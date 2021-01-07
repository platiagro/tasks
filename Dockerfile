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
    apt-get install -y aria2 jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./artifacts/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./config.json /samples/config.json
RUN jq -c ".[] | .artifacts" /samples/config.json | while read artifacts; do \
        echo $artifacts | jq -c ".[]" | while read a; do \
        URL=$(echo $a | jq -r .url); \
        NAME=$(echo $a | jq -r .name); \
        echo "${URL}" >> urls.txt; \
        echo "    out=${NAME}" >> urls.txt; \
        echo "    split=10" >> urls.txt; \
        echo "    max-connection-per-server=10" >> urls.txt; \
        done; \
    done;\
    aria2c -d /artifacts --input-file=urls.txt

COPY ./artifacts /app/artifacts
COPY ./tasks /samples/
WORKDIR /app/artifacts

ENTRYPOINT ["python", "init.py"]
CMD []
