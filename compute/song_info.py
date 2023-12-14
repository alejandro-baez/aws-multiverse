import json

songs =[]
def song_info(title:str, artist:str,length:int, album:str):
    songs.append({
        'title':title,
        'artist': artist,
        'length':length,
        'album':album
    })
    

    return songs

def lambda_handler(event,context):
    song = song_info('Yellow','Coldplay',265,'Parachutes')
    song_info('High Speed','Coldplay',240,'Parachutes')
    song_info('Shiver','Coldplay',302,'Parachutes')
    song_info('Spark','Coldplay',226,'Parachutes')
    song_info('Trouble','Coldplay',273,'Parachutes')
    song_info('Parachutes','Coldplay',45,'Parachutes')
    song_info('We Never Change','Coldplay',248,'Parachutes')
    song_info('Dont Panic','Coldplay',135,'Parachutes')

    message = f"The songs length is {len(song)}"

    return {'statusCode':200,'body': json.dumps({'message': message, 'songs' :song})}
    
