FROM python:3.9.7-alpine3.14
COPY /minitulip .
RUN python3 -m pip install re