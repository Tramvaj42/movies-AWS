import json
import boto3
import urllib3

API_key = "30e30c6c"
API_url = 'https://www.omdbapi.com/'

s3 = boto3.resource("s3")


def lambda_handler(event, context):

    get_messages(event['Records'])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def get_messages(records):
    """
    Function, which will get message from SQS with movies data, enriches them 
    with data from 'https://www.omdbapi.com/' and saves them to S3-sap-interview-assignment
    :param records: meessage from SQS with movies data
    :return:
    """
    for record in records:
        top_10_movies = json.loads(record["body"])

        for movie in top_10_movies:
            # Parameters for endpoint call
            parameters = {'apikey': API_key, 'i': movie['id']}
            # Endpoint call
            http = urllib3.PoolManager()
            resp = http.request("GET", API_url, fields=parameters)
            # Enrich movies with data from endpoint call
            data = json.loads(resp.data.decode('utf-8'))
            movie.update(data)

        file = s3.Object('sap-interview-assignment', 'enriched_top_10_movies.json')
        result = file.put(Body=json.dumps(top_10_movies))
