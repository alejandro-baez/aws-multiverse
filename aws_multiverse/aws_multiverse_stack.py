from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda,
    aws_apigateway as apigateway, 

    # aws_sqs as sqs,
)
from constructs import Construct  



class AwsMultiverseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "AwsMultiverseQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        song_info_funtion = aws_lambda.Function(self, id= 'SongNameFunc', code= aws_lambda.Code.from_asset("./compute/"), handler = 'song_info.lambda_handler',runtime = aws_lambda.Runtime.PYTHON_3_8)

        api = apigateway.RestApi(self,id="restapi", rest_api_name="get-song-api") 
        
        songs = api.root.add_resource('songs')  
        songs.add_method("GET",apigateway.LambdaIntegration(song_info_funtion))
        songs 


        # get_song_integration = apigateway.LambdaIntegration(song_info_funtion,
        #         request_templates={"application/json": '{ "statusCode": "200" }'})

        # api.root.add_method("GET", get_song_integration)   # GET /
       