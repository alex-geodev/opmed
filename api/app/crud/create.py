from app.schema.nine_line import NineLineBase
from app.config import settings
from app.crud.helper import nineLineHelper, send_to_db
import uuid
import vosk
import os
from pydub import AudioSegment


###################################################################
#################### SQLITE Create Methods ########################
###################################################################

vosk_model = vosk.Model(settings.VOSK_MODEL_PATH)
audio_model = vosk.KaldiRecognizer(vosk_model, 16000)

def audio_2_nine_line(audio_file) -> NineLineBase:
    """
    The purpose of this method is to convert from audio file to a 9 line json.
    """
    doc = {}
    doc['id'] = str(uuid.uuid4()).replace('-','')
    doc['audio_path'] = os.getcwd() + audio_file.filename


    try:
        # Remove old file
        try:
            os.remove(audio_file.filename)
            os.remove("temp.wav")
        except:
            pass

        # Save new file
        with open(audio_file.filename, 'wb') as f:
            while contents := audio_file.file.read():
                f.write(contents)

        # Reformat for better performance
        temp = AudioSegment.from_wav(audio_file.filename)
        temp = temp.set_channels(1)
        temp = temp.set_frame_rate(16000)

        # Save new audio
        temp.export("temp.wav", format="wav")

        # Open the audio file
        with open("temp.wav", "rb") as audio:
            while True:
                # Read a chunk of the audio file
                data = audio.read()
                if len(data) == 0:
                    break
                # Recognize the speech in the chunk
                audio_model.AcceptWaveform(data)

        # Get the final recognized result
        result = audio_model.FinalResult()
        result = eval(result)
        doc['audio_translation'] = result['text']


        return doc
    except Exception as e:
        print(e)

def process_nine_line(data:dict)->dict:
    nine_line = nineLineHelper(id = data.get('id'),
                               filepath = data.get('audio_path'),
                               transcription=data.get('audio_translation'))
    
    return nine_line.nineLineProcessed

def write_to_db(processed_nine_line:dict):
    """
    The purpose of this method is to create a nine line object in the database.
    """
    send_to_db(processed_nine_line)

###################################################################
##################### NEO4J Create Methods ########################
###################################################################