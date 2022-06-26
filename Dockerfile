FROM python:3.10-alpine3.16

WORKDIR /src
COPY . /src

RUN mkdir /src/api/data && \
touch /src/api/data/feeds.yaml && \
apk add --no-cache build-base python3-dev curl && \
pip install --upgrade pip && \
python3 -m pip install -r /src/requirements.txt 

EXPOSE 6000

HEALTHCHECK --interval=30s --start-period=5s --retries=3 CMD curl --fail http://0.0.0.0:6000/health || exit 1

CMD ["python3", "/src/api/app.py"]
