import boto3
import time
import os
from base64 import b64decode

s3 = boto3.resource('s3')
#s3_bucket_encrypted = os.environ['S3_BUCKET']
#s3_bucket_decrypted = boto3.client('kms').decrypt(CiphertextBlob=b64decode(s3_bucket_encrypted))['Plaintext']
#s3_bucket = s3_bucket_decrypted
s3_bucket = os.environ['S3_BUCKET']

def print_page(event, context):
	epoch_time = int(time.time())
	print(f'Parsing the event:\n{event}')
	print(f'The epoch time is: {epoch_time}')
	print(f'The S3 bucket is: {s3_bucket}')

	if epoch_time % 2 == 0:
		object = 'index.html'
	else:
		object = 'xedni.html'

	s3_object = s3.Object(bucket_name=s3_bucket, key=object)
	print('The S3 object is: ' + s3_object.bucket_name + '/' + s3_object.key)

	response = s3_object.get()
	data = response['Body'].read().decode('utf-8')

	return {
		'statusCode': 200,
		'body': data
	}
