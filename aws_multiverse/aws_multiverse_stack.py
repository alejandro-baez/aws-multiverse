from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda,
    aws_apigateway as apigateway, 
)
from constructs import Construct  


class AwsMultiverseStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

       
        song_info_funtion = aws_lambda.Function(self, id= 'SongNameFunc', code= aws_lambda.Code.from_asset("./compute/"), handler = 'song_info.lambda_handler',runtime = aws_lambda.Runtime.PYTHON_3_8)

        api = apigateway.RestApi(self,id="restapi", rest_api_name="get-song-api") 
        
        songs = api.root.add_resource('songs')  
        songs.add_method("GET",apigateway.LambdaIntegration(song_info_funtion))
        songs.add_method("POST")


        song = songs.add_resource("{id}")
        song.add_method("GET")
        song.add_method("PUT")
        song.add_method("DELETE")
        

       