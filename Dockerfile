FROM python:3.10.14-alpine

WORKDIR /opt/api

RUN apk add zip

COPY ./api/* /opt/api/

# RUN unzip dependencies/vosk-model-en-us-0.22.zip

RUN pip3 install -r requirements.txt --verbose

# TODO add the dependencies back in when ready
# RUN pip3 install dependencies/vosk-0.3.42-py3-none-linux_riscv64.whl

CMD [ "uvicorn app.main:app --reload" ]

EXPOSE 8000