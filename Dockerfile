# develop stage
FROM node:18.20-alpine

RUN apk update && apk add bash
RUN apk add --no-cache python3 py3-pip

WORKDIR /opt/ui
COPY ./ui/ .
RUN npm install
RUN yarn global add @quasar/cli

RUN python3 -m venv /opt/python/opmed
RUN echo 'manylinux1_compatible = True' > /opt/python/opmed/lib/python3.12/site-packages/_manylinux.py
RUN /opt/python/opmed/bin/python -c 'import sys; sys.path.append(r"/_manylinux.py")'


WORKDIR /opt/api
COPY ./api/ .
RUN /opt/python/opmed/bin/pip install -r requirements.txt

CMD ["/opt/python/opmed/bin/python",  "-m",  "uvicorn", "app.main:app",  "--reload"]

EXPOSE 8000
EXPOSE 8080