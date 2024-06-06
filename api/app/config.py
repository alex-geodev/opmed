from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = 'Stitched Up'
    ROOT_PATH: str = ''
    CORS_ORIGINS: str = '*'

    ###########################################
    ############# SQLITE CONFIG ###############
    ###########################################

    DATABASE_NAME : str = "database.db"

    ###########################################
    ############### Vosk Config ###############
    ###########################################
    VOSK_MODEL_PATH: str = '/Users/nmaynard/Development/op_med_api/vosk-model-en-us-0.22'

    ###########################################
    ######### Object Store Config #############
    ###########################################
    MINIO_URL = 'http://localhost:9000'
    MINIO_BUCKET = 'recordings'

    class Config:
        env_file = '.env'

settings = Settings()
