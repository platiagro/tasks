# PlatIAgro Native Tasks

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Task | Status
--- | ---
[AutoML Classifier](tasks/automl-classifier/) | ![AutoML Classifier](https://github.com/platiagro/tasks/workflows/AutoML%20Classifier/badge.svg)
[AutoML Regressor](tasks/automl-regressor/) | ![AutoML Regressor](https://github.com/platiagro/tasks/workflows/AutoML%20Regressor/badge.svg)
[Face Detection](tasks/cv-mtcnn-face-detection/) | ![Face Detection](https://github.com/platiagro/tasks/workflows/Face%20Detection/badge.svg)
[OCR](tasks/cv-ocr/) | ![OCR](https://github.com/platiagro/tasks/workflows/OCR/badge.svg)
[YOLO](tasks/default-yolo/) | ![YOLO](https://github.com/platiagro/tasks/workflows/YOLO/badge.svg)
[Descriptive Analysis](tasks/descriptive-analysis/) | ![Descriptive Analysis](https://github.com/platiagro/tasks/workflows/Descriptive%20Analysis/badge.svg)
[Featuretools](tasks/feature-tools/) | ![Featuretools](https://github.com/platiagro/tasks/workflows/Featuretools/badge.svg)
[Filter Selection](tasks/filter-selection/) | ![Filter Selection](https://github.com/platiagro/tasks/workflows/Filter%20Selection/badge.svg)
[Grouping Categorical Features](tasks/grouping-categorical-features/) | ![Grouping Categorical Features](https://github.com/platiagro/tasks/workflows/Grouping%20Categorical%20Features/badge.svg)
[Imputer](tasks/imputer/) | ![Imputer](https://github.com/platiagro/tasks/workflows/Imputer/badge.svg)
[Isolation Forest Clustering](tasks/isolation-forest-clustering/) | ![Isolation Forest Clustering](https://github.com/platiagro/tasks/workflows/Isolation%20Forest%20Clustering/badge.svg)
[KMeans Clustering](tasks/kmeans-clustering/) | ![KMeans Clustering](https://github.com/platiagro/tasks/workflows/KMeans%20Clustering/badge.svg)
[Linear Regression](tasks/linear-regression/) | ![Linear Regression](https://github.com/platiagro/tasks/workflows/Linear%20Regression/badge.svg)
[Logistic Regression](tasks/logistic-regression/) | ![Logistic Regression](https://github.com/platiagro/tasks/workflows/Logistic%20Regression/badge.svg)
[MLP Classifier](tasks/mlp-classifier/) | ![MLP Classifier](https://github.com/platiagro/tasks/workflows/MLP%20Classifier/badge.svg)
[MLP Regressor](tasks/mlp-regressor/) | ![MLP Regressor](https://github.com/platiagro/tasks/workflows/MLP%20Regressor/badge.svg)
[English Sentence Classification](tasks/nlp-english-glove-embeddings-sentence-classification/) | ![English Sentence Classification](https://github.com/platiagro/tasks/workflows/English%20Sentence%20Classification/badge.svg)
[MarianMT Translator](tasks/nlp-marianmt-translator/) | ![MarianMT Translator](https://github.com/platiagro/tasks/workflows/MarianMT%20Translator/badge.svg)
[Portuguese Sentence Classification](tasks/nlp-portuguese-glove-embeddings-sentence-classification/) | ![Portuguese Sentence Classification](https://github.com/platiagro/tasks/workflows/Portuguese%20Sentence%20Classification/badge.svg)
[Text Pre-processor](tasks/nlp-text-pre-processor/) | ![Text Pre-processor](https://github.com/platiagro/tasks/workflows/Text%20Pre-processor/badge.svg)
[Normalizer](tasks/normalizer/) | ![Normalizer](https://github.com/platiagro/tasks/workflows/Normalizer/badge.svg)
[Pre Selection](tasks/pre-selection/) | ![Pre Selection](https://github.com/platiagro/tasks/workflows/Pre%20Selection/badge.svg)
[Random Forest Classifier](tasks/random-forest-classifier/) | ![Random Forest Classifier](https://github.com/platiagro/tasks/workflows/Random%20Forest%20Classifier/badge.svg)
[Random Forest Regressor](tasks/random-forest-regressor/) | ![Random Forest Regressor](https://github.com/platiagro/tasks/workflows/Random%20Forest%20Regressor/badge.svg)
[RFE Selector](tasks/rfe-selector/) | ![RFE Selector](https://github.com/platiagro/tasks/workflows/RFE%20Selector/badge.svg)
[Robust Scaler](tasks/robust-scaler/) | ![Robust Scaler](https://github.com/platiagro/tasks/workflows/Robust%20Scaler/badge.svg)
[Simulated Annealing](tasks/simulated-annealing/) | ![Simulated Annealing](https://github.com/platiagro/tasks/workflows/Simulated%20Annealing/badge.svg)
[SVM Classifier](tasks/svc/) | ![SVC](https://github.com/platiagro/tasks/workflows/SVM%20Classifier/badge.svg)
[SVM Regressor](tasks/svr/) | ![SVR](https://github.com/platiagro/tasks/workflows/SVM%20Regressor/badge.svg)
[Transformation Graph](tasks/transformation-graph/) | ![Transformation Graph](https://github.com/platiagro/tasks/workflows/Transformation%20Graph/badge.svg)
[Variance Threshold](tasks/variance-threshold/) | ![Variance Threshold](https://github.com/platiagro/tasks/workflows/Variance%20Threshold/badge.svg)

## Testing

Install the testing requirements:

```bash
apt-get -y install tesseract-ocr tesseract-ocr-por tesseract-ocr-eng
pip install -r requirements.txt
pip install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip install transformers==3.0.2
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
platiagro/datasets:0.2.0
```

Use the following command to run all tests:

```bash
pytest
```
