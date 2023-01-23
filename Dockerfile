FROM python:3.11.0b3-alpine3.16

ADD requirements.txt /

RUN pip install -r requirements.txt

RUN apk update && apk add ffmpeg

COPY . .

CMD [ "python", "./app.py"]

