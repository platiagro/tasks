import json
import tempfile

from minio import Minio

MINIO_CLIENT = Minio(
    endpoint=getenv("MINIO_ENDPOINT", "minio-service.kubeflow:9000"),
    access_key=getenv("MINIO_ACCESS_KEY", "minio"),
    secret_key=getenv("MINIO_SECRET_KEY", "minio123"),
    region=getenv("MINIO_REGION_NAME", "us-east-1"),
    secure=False,
)

with open("/artifacts/config.json") as f:
    artifacts = json.load(f)

for artifact in artifacts:
    print(f"Uploading to MinIO as: {artifact['name']}", flush=True)
    MINIO_CLIENT.fput_object(
        bucket_name="anonymous",
        object_name=f"artifacts/{artifact['name']}",
        file_path=f"/artifacts/{artifact['name']}",
    )

print("done!", flush=True)
