from fetch_facts import get_fact
from generate_voice import generate_voiceover
from create_video import create_video

def main():
    fact = get_fact()
    if fact:
        print(f"Fact: {fact}")
        generate_voiceover(fact, "voiceover.mp3")
        create_video(fact, "voiceover.mp3", "fact_video.mp4")

if __name__ == "__main__":
    main()
