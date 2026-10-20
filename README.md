# Audio & Video Downloader

A simple Python-based downloader that lets you download audio as MP3 files or videos as MP4 files from supported URLs using [`yt-dlp`](https://github.com/yt-dlp/yt-dlp). A folder-selection dialog lets you choose where the downloaded files should be saved.

## Features

- **Audio downloader:** Downloads the best available audio and converts it to MP3 at 320 kbps.
- **Video downloader:** Downloads the best available video and audio streams and merges them into an MP4 file when supported.
- **Multiple URLs:** Enter multiple URLs, separated by commas or by entering each URL on its own line.
- **Choose a destination:** Select the output folder through a graphical folder picker.
- **Windows launchers:** Start either downloader using the included `.bat` files.

## Project Structure

```text
project/
├── audio.bat       # Launches the audio downloader
├── audio.py        # Downloads and converts audio to MP3
├── video.bat       # Launches the video downloader
├── video.py        # Downloads videos and saves them as MP4
└── README.md
```

## Requirements

- Windows (the included `.bat` launchers are intended for Windows)
- Python 3.9 or a compatible version supported by your installed `yt-dlp`
- `yt-dlp`
- FFmpeg available on your system `PATH` for audio conversion and for merging separate video and audio streams

Check that Python is available from Command Prompt:

```bat
py --version
```

Check whether FFmpeg is installed:

```bat
ffmpeg -version
```

If FFmpeg is missing, install it using a trusted source and make sure its executable is available on your system `PATH`.

## Installation

1. **Install Python** if it is not already installed. On Windows, enable the option to add Python to `PATH` if the installer offers it.
2. **Open Command Prompt** or PowerShell in the project directory.
3. **Install the Python dependency:**

   ```bat
   py -m pip install -U yt-dlp
   ```

4. **Install FFmpeg** and ensure that `ffmpeg` is available on your `PATH`.
5. Run one of the launchers described below.

## Usage

### Download audio as MP3

Double-click `audio.bat`, or run:

```bat
py audio.py
```

1. Paste an audio or video URL supported by `yt-dlp` at the `Audio URL:` prompt.
2. Enter additional URLs on new lines, or separate multiple URLs with commas.
3. Press **Enter on an empty line** when you have finished entering URLs.
4. Select the destination folder in the folder-selection dialog.
5. Wait for the downloads and MP3 conversion to finish.

The files are saved in the selected folder. The audio downloader requests the best available audio and converts it to MP3 at a configured quality of 320 kbps.

### Download video as MP4

Double-click `video.bat`, or run:

```bat
py video.py
```

1. Paste a video URL supported by `yt-dlp` at the `Video URL:` prompt.
2. Enter more URLs on separate lines, or separate multiple URLs with commas.
3. Press **Enter on an empty line** when you have finished entering URLs.
4. Select the destination folder in the folder-selection dialog.
5. Wait for the downloads and merging to finish.

The downloader requests the best available video and audio streams and sets the merged output container to MP4 when supported.

## How It Works

- **`audio.py`** uses `yt-dlp` to download audio, Tkinter to select a destination folder, and FFmpeg to extract and convert the audio to MP3.
- **`video.py`** uses `yt-dlp` to download video and audio streams and merge them into an MP4 container when supported.
- **`audio.bat`** launches `audio.py` using the Windows Python launcher.
- **`video.bat`** launches `video.py` using the Windows Python launcher.

## Troubleshooting

### `py` is not recognized

Install Python and ensure the Python launcher is available. You can also try running the script with:

```bat
python audio.py
```

or:

```bat
python video.py
```

### FFmpeg is missing or conversion fails

Install FFmpeg and ensure the directory containing `ffmpeg.exe` is on your system `PATH`. Reopen Command Prompt after changing `PATH`, then check `ffmpeg -version`.

### The folder dialog does not appear

Make sure you are running the script in a desktop session where Tkinter is available. Some minimal Python installations may not include Tkinter.

### A URL fails to download

- Confirm that the URL is correct and accessible.
- Update `yt-dlp` with `py -m pip install -U yt-dlp`.
- Some websites require additional configuration or may change their access methods.
- Check the error printed by `yt-dlp` for more specific information.

### The downloaded file is not MP4 or MP3 as expected

The audio script requires FFmpeg for conversion to MP3. The video script requests an MP4 output container, but the final container and available formats can depend on the source and the codecs supported by the downloaded streams and local FFmpeg installation.

## Notes and Responsible Use

- Download only content you own, have permission to download, or are otherwise legally allowed to save.
- Follow the source website's terms of service and respect copyright and other applicable laws.
- This project relies on `yt-dlp`; compatibility with individual websites can change over time.

## License

No license is specified in this repository. Add a `LICENSE` file if you intend to distribute the project and want to define how others may use it.
