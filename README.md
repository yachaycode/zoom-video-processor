# Zoom Video Downloader

This project is a tool for downloading Zoom meeting videos, extracting audio from those videos, transcribing the audio to text, and curating the transcribed text using LLMs.

## Requirements

- Python 3.x
- `ffmpeg` (must be installed on your system)
- The following Python libraries:
  - `argparse`
  - `subprocess`
  - `requests`
  - `os`
  - `datetime`
  - `whisper`
  - `audio_transcription` (must be implemented in your environment)
  - `audio_extraction` (must be implemented in your environment)

## Installation

1. Clone this repository to your local machine.
2. Install `ffmpeg` on your Linux system:
   ```bash
   sudo apt-get install ffmpeg
   ```
3. Install the necessary Python dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that the functions `transcribe_audio` and `extract_audio_from_video` are implemented in your environment.

## Usage

To download a Zoom video, extract its audio, and transcribe it, run the following command:

```bash
python main.py -url <ZOOM_VIDEO_URL>
```

Replace `<ZOOM_VIDEO_URL>` with the URL of the Zoom meeting you want to download.

## Features

- **Video Download**: Downloads the Zoom meeting video from the provided URL.
- **Audio Extraction**: Extracts audio from the downloaded video.
- **Audio Transcription**: Transcribes the extracted audio to text using `whisper`.
- **Text Curation**: Curates the transcribed text using LLMs.
- **Cleanup**: Deletes the video file after extracting the audio.

## Notes

- Ensure you have the necessary permissions to download and process Zoom content.
- Audio transcription and extraction depend on the implementations of `transcribe_audio` and `extract_audio_from_video`, which must be available in your environment.