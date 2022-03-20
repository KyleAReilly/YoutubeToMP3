from email.mime import base
from pytube import YouTube
from pytube import Playlist
import os
print("\nYouTube To MP3 Format\n")

PlaylistBool = input('Is this a playlist? Y or N:').lower()


def videoDownload():
    if PlaylistBool == 'n':

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

    elif PlaylistBool == 'y':
        URL_ = input("Enter Playlist URL:")
        p = Playlist(URL_)

        try:
            print(f'Downloading: {p.title}')
            for video in p.videos:
                salad = video.streams.filter(only_audio=True).first()
                out_file = salad.download()

                base, ext = os.path.splitext(out_file)
                new_file = base + ".mp3"
                os.rename(out_file, new_file)

            print("\nFiring Missiles")

            print("\nSuccessfully Downloaded\n")

        except:
            print("\nOPE, try again that was wacky")

    loop = input('Would you like to keep converting? Y or N').lower()
    if loop == 'y':
        videoDownload()


videoDownload()
