import requests
from PIL import Image, ImageEnhance
from io import BytesIO

from Error_Logs.log_tools import log_error_to_file

from Secrets.api_keys import VOLUME

def currently_playing(access_token):
    url = 'https://api.spotify.com/v1/me/player/currently-playing'
    headers = {'Authorization': f'Bearer {access_token}'}

    try:
        with requests.get(url, headers=headers, timeout=10) as response:

            if response.status_code == 200:
                data = response.json()
                track_name = data['item']['name']
                artist_name = data['item']['artists'][0]['name']
                album_cover = data['item']['album']['images'][0]['url']
                album_name = data['item']['album']['name']
                progress = data['progress_ms']
                duration = data['item']['duration_ms']
                is_playing = data['is_playing']

                album_image = get_album_cover(url=album_cover, width=32, height=32)

                track_JSON = {
                    'name': track_name,
                    'artist': artist_name,
                    'album_cover': album_image,
                    'album_name': album_name,
                    'progress': progress,
                    'duration': duration,
                    'is_playing': is_playing
                }
                print("successfull")
                return track_JSON
                
        
            elif response.status_code == 403:
                print("currently playing failed: User is not a premium user (required for this operation).")
            elif response.status_code == 204:
                print("currently playing failed: No active device found or track currently playing.")
                return 'no_device_active'
            elif response.status_code == 429:
                log_error_to_file(f"{response.status_code}: {response.content}")
                print("currently playing failed: rate limit.")
            else:
                raise Exception(f"Failed to retrieve data, status code: {response.status_code}")
    except requests.exceptions.Timeout:
        print("Currently playing request timed out.") 
        log_error_to_file('Spotify timed out')
        return 'timed_out'

def get_album_cover(url, width, height):
          try:
               response = requests.get(url)
               response.raise_for_status()  
          except requests.RequestException as e:
               print("error: Failed to retreive image")

          image_data = response.content

          if image_data:
               image = Image.open(BytesIO(image_data))
               image = image.resize((width, height), Image.LANCZOS)
               # Increase the contrast
               enhancer = ImageEnhance.Contrast(image)
               factor = 2  
               image = enhancer.enhance(factor)

               return image

def pause_playback(access_token):
    url = 'https://api.spotify.com/v1/me/player/pause'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Length': '0'
        }

    with requests.put(url, headers=headers) as response:
        if response.status_code == 204:  # Success with no content returned
            print(f"\nPaused Spotify")
        elif response.status_code == 403:
            print("Pause failed: User is not a premium user (required for this operation).")
        elif response.status_code == 404:
            print("Pause failed: No active device found or track currently playing.")
        else:
            raise Exception(f"Failed to pause, status code: {response.status_code}")
    
def resume_playback(access_token):
    url = 'https://api.spotify.com/v1/me/player/play'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Length': '0'
        }

    with requests.put(url, headers=headers) as response:
        if response.status_code == 204:  # Success with no content returned
            print(f"\nResumed Spotify")
        elif response.status_code == 403:
            print("Resume failed: User is not a premium user (required for this operation).")
        elif response.status_code == 404:
            print("Resume failed: No active device found or track paused.")
        else:
            raise Exception(f"Failed to Resume, status code: {response.status_code}")

def set_playback_volume(access_token):
    url = f'https://api.spotify.com/v1/me/player/volume?volume_percent={VOLUME}'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Length': '0'
        }

    with requests.put(url, headers=headers) as response:
        if response.status_code == 204:  # Success with no content returned
            print(f"\nSpotify Volume Set")
        elif response.status_code == 403:
            print("Set Volume failed: User is not a premium user (required for this operation).")
        elif response.status_code == 404:
            print("Set Volume failed: No active device found.")
        else:
            raise Exception(f"Set Volume failed, status code: {response.status_code}")

def skip_to_next(access_token):
    url = 'https://api.spotify.com/v1/me/player/next'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Length': '0'
        }

    with requests.post(url, headers=headers) as response:
        if response.status_code == 204:  # Success with no content returned
            print(f"\nSpotify Skip")
        elif response.status_code == 403:
            print("Spotify Skip failed: User is not a premium user (required for this operation).")
        elif response.status_code == 404:
            print("Spotify Skip failed: No active device found.")
        else:
            raise Exception(f"Spotify Skip failed, status code: {response.status_code}")

def skip_to_previous(access_token):
    url = 'https://api.spotify.com/v1/me/player/previous'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Length': '0'
        }

    with requests.post(url, headers=headers) as response:
        if response.status_code == 204:  # Success with no content returned
            print(f"\nSpotify Previous")
        elif response.status_code == 403:
            print("Spotify Previous failed: User is not a premium user (required for this operation).")
        elif response.status_code == 404:
            print("Spotify Previous failed: No active device found.")
        else:
            raise Exception(f"Spotify Previous failed, status code: {response.status_code}")