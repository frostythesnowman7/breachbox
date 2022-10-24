s3_resource = boto3.resource('s3')
zip_obj = s3_resource.Object(bucket_name="bucket_name_here", key=zip_key)
buffer = BytesIO(zip_obj.get()["Body"].read())

z = zipfile.ZipFile(buffer)
for filename in z.namelist():
    file_info = z.getinfo(filename)
    s3_resource.meta.client.upload_fileobj(
        z.open(filename),
        Bucket=bucket,
        Key=f'{filename}'
    )