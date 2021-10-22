import time
import boto3


DATABASE = 'punto1'
TABLE = 'empresas'
S3_OUTPUT = 's3://bucketpunto1procesado/'
S3_BUCKET = 'bucketpunto1procesado'

def handler(event, context):
    query = 'MSCK REPAIR TABLE `empresas`;'
    client = boto3.client('athena')

    # Execution
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': DATABASE
        },
        ResultConfiguration={
            'OutputLocation': S3_OUTPUT,
        }
    )
    return response