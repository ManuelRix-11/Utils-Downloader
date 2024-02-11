import os


def conv_mp4_to_mp3(mp4) -> None:
    print("Conversione in corso...")
    base, ext = os.path.splitext(mp4)
    mp3 = base + '.mp3'
    os.rename(mp4, mp3)
