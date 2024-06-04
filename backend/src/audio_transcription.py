import wave
import vosk
import json

MODEL_PATH = "../../models/vosk-model-small-en-us-0.15"

model = vosk.Model(MODEL_PATH)

def transcribe_from_wav(wav_path):
    """Transcribe audio from a .wav file.

    Args:
        wav_path (str): Path to .wav file
    Returns:
        str
    """
    wf = wave.open(wav_path, "rb")
    recognizer = vosk.KaldiRecognizer(model, wf.getframerate())
    transcribed = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            transcribed.append(result['text'])

    transcribed.append(json.loads(recognizer.FinalResult())['text'])

    return " ".join(transcribed)

