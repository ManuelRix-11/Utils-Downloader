from pytube import YouTube
from Converter import conv_mp4_to_mp3
import random
import time
import os


def download_video():
    url_vid = input("Inserisci url del video: ")

    yt = YouTube(url_vid, use_oauth=False)
    resolutions = ['720p', '1080p']
    stream = yt.streams.filter(file_extension='mp4',
                               type='video', resolution=resolutions, progressive=True)
    video = stream.get_highest_resolution()

    print("Download del video: \nTitolo: ", yt.title,
          "\nAutore: ", yt.author, "\nLunghezza: ", time.strftime('%H:%M:%S', time.gmtime(yt.length)), "\nRisoluzione: ", video.resolution, "\n")

    print("Download in corso...")
    print("Attendere...")

    video.download(output_path="./output")

    print("Download completato!")


def download_audio():
    url_audio = input("Inserisci url dell' audio: ")

    yt = YouTube(url_audio, use_oauth=False)
    stream = yt.streams.filter()
    audio = stream.get_audio_only()

    print("Estrazione dell'audio: \nTitolo:", yt.title,
          "\nAutore: ", yt.author, "\nLunghezza: ", time.strftime('%H:%M:%S', time.gmtime(yt.length)), "\nBitrate: ", audio.bitrate, "\nCodec: ", audio.audio_codec, "\n")

    print("Download in corso...")
    print("Attendere...")

    file = audio.download(output_path='./output')

    print("Download completato!")

    choice = input("Convertire in mp3? (y/n)\n")

    if choice == 'y' or choice == 'Y':
        conv_mp4_to_mp3(file)
        print("Conversione completata")
