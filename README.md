# PlatIAgro Native Tasks

[![Build Status](https://github.com/platiagro/tasks/workflows/Python%20application/badge.svg)](https://github.com/platiagro/tasks/actions?query=workflow%3A%22Python+application%22)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)


    └── automl-classifier
        ├── Experiment.ipynb      <- Scripts to train models
        └── Deployment.ipynb      <- Scripts to make predictions

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

Use the following command to run all tests:

```bash
pytest
```
