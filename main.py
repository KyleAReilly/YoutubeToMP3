from email.mime import base
from pytube import YouTube
import os
print("\nYouTube To MP3 Format\n")

URL = input("Enter Video URL:")
yt = YouTube(URL)

try:
    print("\nFiring Missiles")
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()

    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)
    print("\nSuccessfully Downloaded\n")

except:
    print("\nOPE, try again that was wonky")