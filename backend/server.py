from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai import AzureOpenAI
import subprocess
import uuid 
app = FastAPI()
origins = ["*"]
client = AzureOpenAI(
    api_key="1D4o8sFEaZYyewJzZWRYeCacUqI2V4KsuAnEcvK4WR0ePuiP7toRJQQJ99AJACYeBjFXJ3w3AAABACOGzORz",
    azure_endpoint="https://windazure.openai.azure.com",
        api_version="2024-08-01-preview",

)

prompt = "Write only the Raw Manim code nothing before it and after it no ```python or nothing just code in Python to "

response = client.chat.completions.create(
    model="gpt-4o-mini",  # Replace with your desired model name
    messages=[{"role": "user", "content": prompt}]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_the_video")
def getTheVideo(prompt:str):
    manim_code = response.choices[0].message.content
    print(manim_code)

    filename = f"./{uuid.uuid4()}.py"
    with open(filename, "w") as file:
        file.write(manim_code)

    print(f"Manim code saved to {filename}")

    try:
        subprocess.run(["manim", "-pql", filename, "SineWave"], check=True)  # Replace 'SineWave' with the appropriate scene name
        print("Video generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating video: {e}")
    return filename