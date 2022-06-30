FROM python:3.10-alpine3.16

WORKDIR /src
COPY . /src

RUN mkdir /src/api/data && \
touch /src/api/data/feeds.json && \
apk add curl && \
pip install --upgrade pip && \
python3 -m pip install -r /src/requirements.txt 

EXPOSE 5000

HEALTHCHECK --interval=30s --start-period=5s --retries=3 CMD curl --fail http://0.0.0.0:5000/health || exit 1

ENTRYPOINT [ "python3" ]
CMD [ "/src/api/app.py" ] 
