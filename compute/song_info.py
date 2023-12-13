import json

def song_info(title:str, artist:str,length:int, album:str):
    song = {
        'title':title,
        'artist': artist,
        'length':length,
        'album':album
    }

    return song

def lambda_handler(event,context):
    song = song_info('Yellow','Coldplay',265,'Parachutes')
    message = f"The songs name is {song['title']}"

    return {'statusCode':200,'body': json.dumps({'message': message, 'song' :song})}
    
