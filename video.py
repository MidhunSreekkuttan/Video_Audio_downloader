from yt_dlp import YoutubeDL
from tkinter import Tk, filedialog
import os

def download_video(urls):
    # Hide the Tkinter window
    root = Tk()
    root.withdraw()

    # Select download folder
    download_folder = filedialog.askdirectory(
        title="Select Download Folder"
    )
    root.destroy()

    if not download_folder:
        print("Download cancelled: No folder selected.")
        return

    options = {
        "format": "bv*+ba/b",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(
            download_folder, "%(title)s.%(ext)s"
        ),
    }

    with YoutubeDL(options) as ydl:
        ydl.download(urls)

    print(f"\nDownload completed! Saved in: {download_folder}")


if __name__ == "__main__":
    print("=" * 45)
    print("        Video Downloader")
    print("=" * 45)
    print("Paste Video URL below.")
    print("For multiple URLs, paste one per line.")
    print("Press Enter on an empty line when finished.\n")

    urls = []

    while True:
        url = input("Video URL: ").strip()

        if not url:
            break

        # Allow multiple URLs separated by commas
        urls.extend(
            link.strip()
            for link in url.split(",")
            if link.strip()
        )

    if urls:
        download_video(urls)
    else:
        print("No URLs entered. Exiting.")
