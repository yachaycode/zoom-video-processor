import os
import subprocess

def extract_audio_from_video(video_path, audio_path):
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vn',  # No video
        '-acodec', 'libmp3lame',
        '-q:a', '2',  # Calidad de audio
        audio_path
    ]
    subprocess.run(command, check=True)
    print(f"Audio extraído exitosamente en {audio_path}")