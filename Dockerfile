FROM python:alpine

ENV GUNICORN_WORKERS 2
ENV GUNICORN_BACKLOG=4096

RUN pip install gunicorn json-logging-py

COPY ./ /src/app

RUN pip install /src/app

EXPOSE 8000

CMD [ \
    "/usr/local/bin/gunicorn", \
    "--config", "/src/app/config/gunicorn.py", \
    "--log-config", "/src/app/config/logger.conf", \
    "-b", ":8000", \
    "quotes.app:APP" \
]
