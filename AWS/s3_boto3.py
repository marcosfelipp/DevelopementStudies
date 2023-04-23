import boto3

if __name__ == "__main__":
    s3 = boto3.client("s3")

    bucket_name = "test-bucket-boto3-marcos"

    # Create bucket
    s3.create_bucket(Bucket=bucket_name)

    # List buckets
    buckets = s3.list_buckets()
    for bucket in buckets["Buckets"]:
        print(bucket)

    # Upload file to bucket
    with open("image.jpeg", "rb") as img:
        s3.upload_fileobj(img, bucket_name, "image.jpeg")

    print(s3.list_objects(Bucket=bucket_name)["Contents"])

    # Delete object
    s3.delete_object(Bucket=bucket_name, Key='image.jpeg')

    # Delete bucket
    s3.delete_bucket(Bucket=bucket_name)