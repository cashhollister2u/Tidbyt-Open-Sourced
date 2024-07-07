from .auth import refresh_access_token

def spotify_player(player_callback_function, set_spotify_access_token, access_token, refresh_token, channel):
    try:
        if channel == 'currently_playing':
            currently_playing = player_callback_function(access_token)
            return currently_playing
    except Exception as e:
        print(f"Exception occurred: {e}")
        print('Access token expired')            
        access_token = refresh_access_token(refresh_token)
        if set_spotify_access_token != None:
            set_spotify_access_token(access_token) # will refresh every call after init access token expires without 
        if channel == 'currently_playing':
            currently_playing = player_callback_function(access_token)
            return currently_playing