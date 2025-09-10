from google.cloud import storage

bucket_name = "my_buckets_mlops"
source_blob_name = "Hotel_Reservations.csv"
destination_file_name = "Hotel_Reservations.csv"

client = storage.Client()
bucket = client.bucket(bucket_name)
blob = bucket.blob(source_blob_name)

try:
    blob.download_to_filename(destination_file_name)
    print("✅ Download successful")
except Exception as e:
    print("❌ Download failed:", e)
