import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language='es')  # Especificar el idioma español
    print("Transcripción del audio:")
    print(result['text'])