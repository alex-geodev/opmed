from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = 'Hackathon'
    ROOT_PATH: str = ''
    CORS_ORIGINS: str = '*'

    ###########################################
    ############ Elastic Config ###############
    ###########################################

    ELASTIC_URL = 'http://localhost:9200'
    NINE_LINE_INDEX: str = 'nine_line'

    ###########################################
    ############### Vosk Config ###############
    ###########################################
    VOSK_MODEL_PATH: str = '/Users/alex/Dev/vosk/vosk-model-en-us-0.22'

    ###########################################
    ######### Object Store Config #############
    ###########################################
    MINIO_URL = 'http://localhost:9000'
    MINIO_BUCKET = 'recordings'

    class Config:
        env_file = '.env'

settings = Settings()
