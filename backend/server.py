from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import AzureOpenAI
import subprocess
import uuid 
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from pydantic import BaseModel
from pydantic_ai import Agent
import ast

import re
import asyncio

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

class ManimCode(BaseModel):
    code: str

agent = Agent(
    "gemini-2.0-flash-exp",
    result_type=ManimCode,
    system_prompt="Write only the Raw Manim code nothing else to create an intuitive animation for",
)

app.mount("/directory", StaticFiles(directory=Path("directory"), html=True), name="directory")

origins = ["*"]
client = AzureOpenAI(
    api_key="1D4o8sFEaZYyewJzZWRYeCacUqI2V4KsuAnEcvK4WR0ePuiP7toRJQQJ99AJACYeBjFXJ3w3AAABACOGzORz",
    azure_endpoint="https://windazure.openai.azure.com",
        api_version="2024-08-01-preview",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def sanitize_code_output(code_output: str) -> str:
    """
    Sanitize the output from LLM by removing Markdown code block indicators
    only if they are present.

    Args:
        code_output (str): The raw output from the LLM.

    Returns:
        str: The sanitized code without Markdown formatting, or the original input if no indicators are found.
    """
    # Check if the input contains the Markdown code block indicators
    if "```python" in code_output and "```" in code_output:
        # Remove the Markdown code block indicators
        sanitized_output = (
            code_output.replace("```python", "")
            .replace("```", "")
            .strip()
        )
        return sanitized_output
    else:
        return code_output  # Return as is if no indicators are found




@app.get("/get_the_video")
async def getTheVideo(prompt: str):
    prompt = "Write only the Raw Manim code intuitive animations for " + prompt

    # response = client.chat.completions.create(
    #     model="gpt-4o",  # Replace with your desired model name
    #     messages=[{"role": "user", "content": prompt}]
    # )

    response_agent = await agent.run(prompt)
    print(response_agent.data.code.encode().decode('unicode_escape'))

    
    manim_code = response_agent.data.code
    # print(manim_code)

    filename = f"{uuid.uuid4()}"
    with open("./"+filename+".py", "w") as file:
        file.write(str(manim_code.replace("\\n", "\n")).encode().decode('unicode_escape'))

    print(f"Manim code saved to {filename}")

    # Extracting the scene name from the manim_code
    scene_name_match = re.search(r'class (\w+)\(Scene\)', manim_code)
    if scene_name_match:
        scene_name = scene_name_match.group(1)
        video_filename = f"{scene_name}.mp4"  # Assuming default output format is .mp4
    else:
        video_filename = "unknown_scene.mp4"

    try:
        subprocess.run(["manim", "-ql", "./"+filename+".py", "-a"], check=True)  # Replace 'SineWave' with the appropriate scene name
        print("Video generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating video: {e}")
        return {"error": str(e), "video_name": None}

    return {"video_name": f"directory/videos/{filename}/480p15/{video_filename}"}