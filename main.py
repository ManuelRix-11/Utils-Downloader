from Downloader import *

if __name__ == "__main__":
    print("1. Download Video\n 2. Download Audio")
    choice = input("Cosa si vuole fare?\n")
    if int(choice) == 1:
        download_video()
    if int(choice) == 2:
        download_audio()
