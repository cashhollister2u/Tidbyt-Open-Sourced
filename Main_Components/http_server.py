from flask import Flask, jsonify
import json
import time

from Main_Components.user_data import User, ShareUser
from Api_Connections.spotify.auth import get_user_authorization, get_spotify_refresh
from Bash_Scripts.off_command import off_switch

from Error_Logs.log_tools import log_error_to_file

app = Flask(__name__)

# more gracefull transfer of class data after user is created
shared_user = ShareUser()

alt_views = ['req_spot_auth', 'req_stock_api_key', 'req_weather_api_key', 'no_device_active', 'invalid_stock', 'invalid_zipcode']

# set initial api parametes and init data collection 
@app.route('/start/<string:client_id>/<string:stock>/<int:zip_code>/<string:channel>/<float:brightness>')
def start_user_thread(client_id:str, stock:str, zip_code:int, channel:str, brightness:int):
     user = shared_user.get_user()
     try:
          # access refresh token saved to .json file
          with open("Secrets/spotify_refresh_token.json", 'r') as file:
               refresh_token = json.load(file)
               refresh_token = refresh_token['refresh_token']
     except:
          refresh_token = None
     
     if user == None:
          user = User(client_id=client_id, stock=stock, zip_code=zip_code, channel=channel, spotify_refresh_token=refresh_token, brightness=int(brightness))
          user.set_spotify_access_token()
          # pass user to main after created
          shared_user.set_user(user)
          response = user.create_thread()
          
          # withhold http responce till data is loaded for views / alt views
          while user.displayLoaded != channel and user.displayLoaded not in alt_views:
               time.sleep(1)
          return response
     else:
          return jsonify(f"User already retreiving data"), 404 


# update api parameters for data collection 
@app.route('/update/<string:client_id>/<string:stock>/<int:zip_code>/<float:brightness>')
def update_user_thread(client_id:str, stock:str, zip_code:int, brightness:int):
     user = shared_user.get_user()
     if user:
          # update the data saved on device 
          with open("Secrets/user_inputs.json", "r") as file:
               data = json.load(file)
               data["zip_code"] = zip_code
               data["stock"] = stock

          with open("Secrets/user_inputs.json", 'w') as file:
               json.dump(data, file, indent=4)

          return user.update_thread(client_id=client_id, stock=stock, zip_code=zip_code, brightness=100)
     else:
          return jsonify(f"User {client_id} not found"), 404 
     

# switch led display
@app.route('/channel/<string:client_id>/<string:channel>')
def update_user_channel(client_id:str, channel:str):
     user = shared_user.get_user()
     # updates channel 
     try:
          response = user.update_channel(channel) 

          # update the data saved on device 
          with open("Secrets/user_inputs.json", "r") as file:
               data = json.load(file)
               data["channel"] = channel

          with open("Secrets/user_inputs.json", 'w') as file:
               json.dump(data, file, indent=4)

          # withhold http responce till data is loaded
          while user.displayLoaded != channel and user.displayLoaded not in alt_views:
               time.sleep(1)
          return response
     
     except Exception as e:
          print(e)
          return jsonify(f"User {client_id} not found"), 404 
     

# Spotify auth Process
@app.route('/auth_url')
def get_spotify_auth_url():
     try:
          auth_url = get_user_authorization()
          return auth_url, 200
     except Exception as e:
          log_error_to_file(e)
          

# Spotify auth Process
@app.route('/spotify_refresh/<string:auth_code>')
def get_spotify_refresh_token(auth_code:str):
     user = shared_user.get_user()
     try:
          refresh_token = {
               "refresh_token":get_spotify_refresh(auth_code)
          } 
          
          with open("Secrets/spotify_refresh_token.json", 'w') as file:
               json.dump(refresh_token, file)

          # updates token mid session
          if user != None:
               user.spotify_refresh_token = refresh_token['refresh_token']
          return jsonify(f"Spotify Authenticated"), 204
    
     except Exception as e:
          return jsonify(error=f"An error occurred: {e}"), 500
     

@app.route("/turn_off/<string:client_id>")
def turn_off_display(client_id:str):
     user = shared_user.get_user()
     
     if user == None:
          off_switch() 
          return jsonify(f"Shut Down Complete"), 204
     elif user.client_id == client_id:
          off_switch()
          return jsonify(f"Shut Down Complete"), 204
     else:
          return jsonify(f"Invalid client id"), 404


# exported to be called in main as a threaded instance
def run_flask_server():
    app.run(host="0.0.0.0", port=6000, debug=False, use_reloader=False, threaded=False)

