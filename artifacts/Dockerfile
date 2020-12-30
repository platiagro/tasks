FROM python:3.7-buster

LABEL maintainer="fabiol@cpqd.com.br"

# Stamps the commit SHA into the labels and ENV vars
ARG BRANCH="master"
ARG COMMIT=""
LABEL branch=${BRANCH}
LABEL commit=${COMMIT}
ENV COMMIT=${COMMIT}
ENV BRANCH=${BRANCH}

RUN apt-get update && \
    apt-get install wget unzip jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install "minio>=5.0.6,<6.0.0"

COPY ./config.json /artifacts/config.json

RUN jq -c ".[]" /artifacts/config.json | while read a; do \
    URL=$(echo $a | jq -r .url); \
    FILE_PATH=$(echo $a | jq -r .file_name); \
    wget -O "$FILE_PATH" "$URL"; \
    done

COPY ./init.py /app/init.py

WORKDIR /app/

ENTRYPOINT ["python", "/app/init.py"]
CMD []
