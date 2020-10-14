# PlatIAgro Native Tasks

[![Build Status](https://github.com/platiagro/tasks/workflows/Python%20application/badge.svg)](https://github.com/platiagro/tasks/actions?query=workflow%3A%22Python+application%22)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


    ├── automl-classifier
    │   ├── Experiment.ipynb      <- Scripts to train models
    │   └── Deployment.ipynb      <- Scripts to make predictions
    ├── automl-regressor
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── logistic-regression
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── linear-regression
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── svc
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── svr
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── mlp-classifier
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── mlp-regressor
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── random-forest-classifier
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── random-forest-regressor
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── descriptive-analysis
    │   └── Experiment.ipynb
    ├── feature-tools
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── filter-selection
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    ├── grouping-categorical-features
    │   ├── Experiment.ipynb
    │   └── Deployment.ipynb
    └── imputer
        ├── Experiment.ipynb
        └── Deployment.ipynb

## Testing

Install the testing requirements:

```bash
pip install -r requirements.txt
```

Export these environment variables:

```bash
export MINIO_ENDPOINT=localhost:9000
export MINIO_ACCESS_KEY=minio
export MINIO_SECRET_KEY=minio123
```

Start MinIO and Datasets API:

```bash
docker network create tasks
```

```bash
docker run -d -p 9000:9000 \
--name minio \
-e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
-e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
--network tasks \
minio/minio:RELEASE.2018-02-09T22-40-05Z server /data
```

```bash
docker run -d -p 8080:8080 \
--name datasets \
-e "MINIO_ENDPOINT=minio:9000" \
-e "MINIO_ACCESS_KEY=$MINIO_ACCESS_KEY" \
-e "MINIO_SECRET_KEY=$MINIO_SECRET_KEY" \
--network tasks \
platiagro/datasets:0.1.0
```

Use the following command to run all tests:

```bash
pytest
```
