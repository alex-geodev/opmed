# Med OP API

The purpose of this repo is to host an api for methods related to the Med OP hackathon project. This currently includes the following


## Features

- Conversion from Audio to Nine Line Object

## Setup

```
pip install -r requirements.txt
wget https://alphacephei.com/vosk/models/vosk-model-en-us-0.22.zip
unzip vosk-model-en-us-0.22.zip
uvicorn app.main:app --reload
```

From here you should be able to navigate to localhost:8000/docs which will display the U.I.

## Building Container

You should be able to build the container like so:

```
docker build -t dorad:latest .
```

## Running Container

The container can be run like so

```
docker run
```