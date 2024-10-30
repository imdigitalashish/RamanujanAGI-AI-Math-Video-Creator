from openai import AzureOpenAI 
import os

import subprocess
os.environ["OPENAI_API_VERSION"] = "2023-12-01-preview"
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://windazure.openai.azure.com"
os.environ["AZURE_OPENAI_API_KEY"] = "1D4o8sFEaZYyewJzZWRYeCacUqI2V4KsuAnEcvK4WR0ePuiP7toRJQQJ99AJACYeBjFXJ3w3AAABACOGzORz"

client = AzureOpenAI(
    api_key="1D4o8sFEaZYyewJzZWRYeCacUqI2V4KsuAnEcvK4WR0ePuiP7toRJQQJ99AJACYeBjFXJ3w3AAABACOGzORz",
    azure_endpoint="https://windazure.openai.azure.com",
        api_version="2024-08-01-preview",

)
prompt = "Write only the Raw Manim code nothing before it and after it no ```python or nothing just code in Python to "

# Call the completion endpoint
response = client.chat.completions.create(
    model="gpt-4o-mini",  # Replace with your desired model name
    messages=[{"role": "user", "content": prompt}]
)

# Print the assistant's response
manim_code = response.choices[0].message.content
print(manim_code)

filename = "sine_wave_animation.py"
with open(filename, "w") as file:
    file.write(manim_code)

print(f"Manim code saved to {filename}")

# Step 2: Run the Manim code to generate the video
# Adjust the command below if your Manim installation requires different arguments
try:
    subprocess.run(["manim", "-pql", filename, "SineWave"], check=True)  # Replace 'SineWave' with the appropriate scene name
    print("Video generated successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error generating video: {e}")