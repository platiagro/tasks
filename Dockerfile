FROM python:3.7-buster

LABEL maintainer="fabiol@cpqd.com.br"

# Stamps the commit SHA into the labels and ENV vars
ARG BRANCH="main"
ARG COMMIT=""
LABEL branch=${BRANCH}
LABEL commit=${COMMIT}
ENV COMMIT=${COMMIT}
ENV BRANCH=${BRANCH}

RUN apt-get update && \
    apt-get install -y aria2 jq && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY ./init-job/requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY ./tasks /tasks
COPY ./config.json /tasks/config.json

# Downloads artifacts in task dir
RUN touch urls.txt; \
    jq -c ".[]" /tasks/config.json | while read TASK; do \
        echo ${TASK} | jq -r ".artifacts" | jq -c ".[]" | while read ARTIFACT; do \
            echo "${ARTIFACT}" | jq -r .url >> urls.txt; \
            printf "    out=" >> urls.txt; \
            printf "${TASK}" | jq -c -r .path | tr -d '\n' >> urls.txt; \
            printf "/" >> urls.txt; \
            printf "${ARTIFACT}" | jq -c -r .name >> urls.txt; \
            echo "    split=10" >> urls.txt; \
            echo "    max-connection-per-server=10" >> urls.txt; \
        done; \
    done; \
    cat urls.txt; \
    aria2c --input-file=urls.txt

COPY ./init-job /app/
WORKDIR /app/

ENTRYPOINT ["python", "main.py"]
CMD []
