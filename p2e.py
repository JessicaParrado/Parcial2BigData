import time
import boto3


DATABASE = 'punto2'
TABLE = 'periodicos'
S3_OUTPUT = 's3://bucketpunto2procesado/LambdaParticion/'
S3_BUCKET = 'bucketpunto2procesado'

def handler(event, context):
    query = 'MSCK REPAIR TABLE `periodicos`;'
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