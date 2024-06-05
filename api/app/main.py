from fastapi import FastAPI
from .config import settings
from .router import api_router
from fastapi.middleware.cors import CORSMiddleware
from . import __version__

app = FastAPI(title=settings.APP_NAME,
              version=__version__,
              root_path=settings.ROOT_PATH
              )

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


app.include_router(api_router, prefix=settings.ROOT_PATH)
