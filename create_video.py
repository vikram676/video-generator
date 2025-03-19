from moviepy.video.io.ImageSequenceClip import ImageSequenceClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_video(text, audio_file, output_file):
    # Create background image
    width, height = 1080, 1920
    img = Image.new('RGB', (width, height), color=(0, 0, 0))

    wrapped_text = textwrap.fill(text, width=30)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 60)

    bbox = draw.textbbox((0, 0), wrapped_text, font=font)
    text_w, text_h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(((width - text_w) / 2, (height - text_h) / 2), wrapped_text, font=font, fill="white")


    img.save("background.png")

    # Load audio
    audio = AudioFileClip(audio_file)
    duration = audio.duration

    # Create video with background and audio
    background = ImageClip("background.png").with_duration(duration).resized(height=1920, width=1080)
    video = background.with_audio(audio)

    video.write_videofile(output_file, codec="libx264", fps=24)

if __name__ == "__main__":
    fact = "Did you know that honey never spoils?"
    create_video(fact, "voiceover.mp3", "fact_video.mp4")
