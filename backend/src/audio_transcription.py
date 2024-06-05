import wave
import vosk
import json
from pydub import AudioSegment
import os

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


def convert_to_wav(m4a_path):

    m4a_file = m4a_path # I have downloaded sample audio from this link https://getsamplefiles.com/sample-audio-files/m4a
    wav_filename = './data/output.wav'

    sound = AudioSegment.from_file(m4a_file, format='m4a')
    file_handle = sound.export(wav_filename, format='wav')

