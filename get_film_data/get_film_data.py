import json
import boto3

s3 = boto3.resource("s3")
sqs = boto3.resource("sqs")


def lambda_handler(event, context):
    
    movies = get_data()

    return {
        'statusCode': 200,
        'body': movies
    }


def get_data():
    """
    Function, which gets movies data from S3 filters top 10 and sends them to SQS
    :return: 
    """
    # Get movie data from S3
    movie_bucket = s3.Object('top-movies', 'Top250Movies.json').get()
    movie_dictionary = json.load(movie_bucket['Body'])
    # Filter top 10 movies
    top_10_movies = [movie for movie in movie_dictionary['items'] if int(movie['rank']) <= 10]
    # Parse movies to json
    top_10_movies = json.dumps(top_10_movies)
    
    # Send data to SQS
    queue = sqs.get_queue_by_name(QueueName='sap_interview_film_queue')
    response = queue.send_message(MessageBody=top_10_movies)
    return top_10_movies
