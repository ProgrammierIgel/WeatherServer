FROM python:3.12.3-alpine3.19

WORKDIR ./src/weather

COPY . .

RUN apk add --no-cache bash

RUN pip install ipython
RUN pip install python-weather
RUN pip install -U Flask
RUN touch location.txt

CMD ["ipython", "./app.py"]