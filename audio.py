from yt_dlp import YoutubeDL
from tkinter import Tk, filedialog
import os


def download_audio(urls):
    # Hide the Tkinter window
    root = Tk()
    root.withdraw()

    # Select download folder
    download_folder = filedialog.askdirectory(
        title="Select MP3 Download Folder"
    )
    root.destroy()

    if not download_folder:
        print("Download cancelled: No folder selected.")
        return

    options = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(
            download_folder, "%(title)s.%(ext)s"
        ),
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "320",
            }
        ],
    }

    with YoutubeDL(options) as ydl:
        ydl.download(urls)

    print(f"\nMP3 downloads completed!")
    print(f"Saved in: {download_folder}")


if __name__ == "__main__":
    print("=" * 45)
    print("         MP3 Downloader")
    print("=" * 45)
    print("Paste Audio URLs below.")
    print("You can enter multiple URLs.")
    print("Press Enter on an empty line when finished.\n")

    urls = []

    while True:
        url = input("Audio URL: ").strip()

        if not url:
            break

        urls.extend(
            link.strip()
            for link in url.split(",")
            if link.strip()
        )

    if urls:
        download_audio(urls)
    else:
        print("No URLs entered. Exiting.")
