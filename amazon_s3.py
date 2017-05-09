

##########################################################################################
#
#   Amazon S3
#
#   https://boto3.readthedocs.io/en/latest/guide/migrations3.html#deleting-a-bucket
#   https://boto3.readthedocs.io/en/latest/guide/quickstart.html
#   https://aws.amazon.com/sdk-for-python/
#
##########################################################################################

'''

First initialize credentials and config:

1.) Create ~/.aws/credentials (chmod 700 ~/.aws)
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY

2.) Create ~/.aws/config
[default]
region=us-east-1

'''



def s3_list_buckets():
    import boto3
    # Create S3 Client
    s3 = boto3.client('s3')
    # List Buckets
    buckets = s3.list_buckets()
    list_of_buckets = [bucket['Name'] for bucket in buckets['Buckets']]
    return list_of_buckets



def s3_get_bucket_acl(bucket_name): # Get Access Permissions
    import boto3
    # Create S3 client
    s3 = boto3.client('s3')
    # Call S3 to get CORS configuration for selected bucket
    permissions = s3.get_bucket_acl(Bucket=bucket_name)
    return permissions



def s3_create_bucket(bucket_name):
    import boto3
    # Create S3 Client
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)



def s3_upload_file(bucket_name, filepath_and_name):
    import boto3
    # Create S3 client
    s3 = boto3.client('s3')
    filename = filepath_and_name
    bucket_name = bucket_name
    # Uploads the given file using a managed uploader, which will split up large
    # files automatically and upload parts in parallel.
    s3.upload_file(filename, bucket_name, filename.split('/')[-1])

s3_upload_file('dzaratsian', '/Users/dzaratsian/Desktop/test.txt')




#ZEND