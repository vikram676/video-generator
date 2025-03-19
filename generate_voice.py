import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

def generate_voiceover(text, output_file):
    url = "https://api.elevenlabs.io/v1/text-to-speech/CwhRBWXzGAHq8TQ4Fs17"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.8
        }
    }

    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Audio saved to {output_file}")
    else:
        print(f"Failed to generate audio: {response.status_code}, {response.text}")

if __name__ == "__main__":
    fact = "Did you know that honey never spoils?"
    generate_voiceover(fact, "voiceover.mp3")
