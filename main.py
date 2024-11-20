import argparse
import os
from download_video_zoom import generate_video_path, generate_audio_path, download_zoom_video
from audio_transcription import transcribe_audio
from audio_extraction import extract_audio_from_video


def parse_arguments():
    parser = argparse.ArgumentParser(description="Download a Zoom video and extract its audio.")
    parser.add_argument('--zoom_url', '-url', type=str, help='La URL de la reunión de Zoom')
    return parser.parse_args()


def main():
    args = parse_arguments()
    video_path = generate_video_path()
    audio_path = generate_audio_path()
    download_zoom_video(args.zoom_url, video_path)
    extract_audio_from_video(video_path, audio_path)
    transcribe_audio(audio_path)
    if os.path.exists(video_path):
        os.remove(video_path)
        print(f"Archivo de video eliminado: {video_path}")

if __name__ == "__main__":
    main()