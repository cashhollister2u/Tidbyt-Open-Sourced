import requests

from Secrets.api_keys import CLIENT_ID, CLIENT_SECRET

# custom urlencode funct
def urlencode(query): 
    def escape(s):
        s = str(s)
        safe_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.-"
        return ''.join([c if c in safe_chars else '%{:02X}'.format(ord(c)) for c in s])

    return '&'.join([f"{escape(k)}={escape(v)}" for k, v in query.items()])

# should only need to be done once 
def get_user_authorization():
    """Directs the user to the Spotify login page for authorization."""
    query_params = {
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': 'http://localhost:8080/',
        'scope': 'user-read-currently-playing user-modify-playback-state', #look at spotify api documentaion for different scopes
    }
    url = f"https://accounts.spotify.com/authorize?{urlencode(query_params)}"
    return url

def get_spotify_refresh(code):
    """Exchange the authorization code for an access token."""
    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': 'http://localhost:8080/',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    
    with requests.post(url, data=data) as response:
        if response.status_code == 200:
            return response.json()['refresh_token']
        
        else:
            print("Failed to retrieve refresh token:", response.json())
            return None

def refresh_access_token(refresh_token):
    """Use the refresh token to obtain a new access token."""
    url = 'https://accounts.spotify.com/api/token'
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    }
    with requests.post(url, data=data) as response:
        if response.status_code == 200:
            new_tokens = response.json()
            print('refreshed token')
            return new_tokens['access_token']
        else:
            print("Failed to refresh access token:", response.json())
            return None

def extract_code_from_url(url):
    """Extracts the authorization code from a given URL or indicates failure."""
    try:
        return url.split("code=")[1].split("&")[0]
    except IndexError:
        print("Failed to extract the authorization code. Please make sure you've entered the correct URL.")
        return None
    