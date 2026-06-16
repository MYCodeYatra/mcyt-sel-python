import os
import boto3
from botocore.exceptions import ClientError
class VisualAssetManager:
    def __init__(self, bucket_name="mycodeyatra-visual-baselines"):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3', region_name='us-east-1')
        self.temp_dir = "temp_baselines"
        # Ensure temporary directory exists
        os.makedirs(self.temp_dir, exist_ok=True)
    def fetch_baseline(self, image_name: str) -> str:
        """Downloads the baseline image from S3 to a temporary local folder."""
        local_path = os.path.join(self.temp_dir, image_name)
        try:
            print(f"\n[S3] Downloading baseline: {image_name}...")
            self.s3_client.download_file(self.bucket_name, image_name, local_path)
            return local_path
        except ClientError as e:
            # If the baseline doesn't exist, this is a new test! We need to approve it.
            if e.response['Error']['Code'] == "404":
                raise FileNotFoundError(f"Baseline {image_name} not found in S3. Needs approval!")
            raise
    def update_baseline(self, local_image_path: str, new_image_name: str):
        """Uploads a new or updated baseline image to S3."""
        print(f"[S3] Uploading updated baseline: {new_image_name}...")
        self.s3_client.upload_file(local_image_path, self.bucket_name, new_image_name)
        print("✅ Baseline successfully updated in the cloud!")