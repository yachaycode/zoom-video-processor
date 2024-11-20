import requests
import os
import datetime


def generate_video_path():
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"data/zoom_video_{date_str}.mp4"


def generate_audio_path():
    date_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"data/zoom_audio_{date_str}.mp3"


def download_zoom_video(zoom_url, video_path):
    os.makedirs(os.path.dirname(video_path), exist_ok=True)
    response = requests.get(zoom_url, stream=True)
    if response.status_code == 200:
        with open(video_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                f.write(chunk)
        print(f"Video descargado exitosamente en {video_path}")
    else:
        print("Error al descargar el video. Verifica el enlace y los permisos.")