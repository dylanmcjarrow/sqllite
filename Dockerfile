FROM python:3.9.7-alpine3.14 
RUN apk update && apk add gcc libc-dev
COPY /minitulip .
COPY /requirements.txt .
COPY /.env .
RUN python3 -m venv .venv
RUN source ./.venv/bin/activate
RUN pip install -r requirements.txt
CMD [ "python3","-m","minitulip.app","-ir" ]