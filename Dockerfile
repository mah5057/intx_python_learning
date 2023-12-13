FROM python:3.11-slim 

ADD . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
RUN mkdir /tmp/prometheus_multiproc
ENV PYTHONPATH='.'

CMD [ "python", "-m", "web_app" ]
