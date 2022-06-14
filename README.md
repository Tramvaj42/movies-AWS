# Movies-AWS
SAP interview assignment

## Description
Application, which runs daily. The task of the application is to acquire the top 250 IMDB movies, filter the top 10, enrich them with more data from The OMDb API, and save them [here](https://sap-interview-assignment.s3.eu-central-1.amazonaws.com/enriched_top_10_movies.json)

## How to use it
The application runs daily and the data are updated at 22:00 (GMT +2). But if you call the endpoint: https://jjso0ccpx6.execute-api.eu-central-1.amazonaws.com/default/get_film_data you will get top-10 movies from IMDB in JSON and consequentially the [final enriched file](https://sap-interview-assignment.s3.eu-central-1.amazonaws.com/enriched_top_10_movies.json) will be updated.

To deploy this application yourself. You should set up an [AWS account](https://aws.amazon.com/free/). You should create two lambda functions—one for the get_film_data function and the other for the enrich_film_data function. Then you should set up an SQS with a trigger to the enrich_film_data function. You should edit the function's code, so you call your SQS and your S3 bucket. After that, you are set to run your get_film_data function, which will consequentially trigger the enrich_movie_data function.

## Resources
- [AWS S3 bucket](https://aws.amazon.com/s3/) 
- [AWS lambda function](https://aws.amazon.com/lambda/) 
- [AWS SQS](https://aws.amazon.com/sqs/) 
- [AWS python library](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) 
- [The OMDb API](http://www.omdbapi.com/) -  RESTful web service to obtain movie information 

## Credits
SAP CAT team 
