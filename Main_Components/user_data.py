import time
from threading import Lock, Thread
from flask import jsonify

# custom components
from Api_Connections.twelve_api import package_stock_data, market_data_sleep_mode
from Api_Connections.weather_api import get_weather
from Api_Connections.spotify.player import spotify_player
from Api_Connections.spotify.player_params import currently_playing
from Api_Connections.spotify.auth import refresh_access_token

from Error_Logs.log_tools import log_error_to_file


# Storage container to pass the user object to main so that it is accessable once created --- imports "None" without impementing "Shareduser"
class ShareUser:
    def __init__(self):
        self.user = None
        self.lock = Lock()

    def set_user(self, user):
        with self.lock:
            self.user = user

    def get_user(self):
        with self.lock:
            return self.user



class User():

     def __init__(self, client_id:str, stock:str, zip_code:int, spotify_refresh_token:str, channel:str, brightness:int=100):
          #### Board api data ####
          self.client_id = client_id
          self.stock = stock
          self.stock_change = True
          self.zip_code = zip_code
          self.location_change = True
          self.spotify_refresh_token = spotify_refresh_token
          self.spotify_access_token = None
          #### Api data package parameters ####
          self.channel = channel
          self.thread = None
          self.api_data = { "weather": None, "stock": None, "spotify": None, "spotify2_image": None }
          #### limit race conditions ####
          self.data_interval = 400 # (10 minutes) ** loop runs at .75 speed of real time **
          self.isDataReady = False
          self.displayLoaded = ""
          self.lock = Lock()
          #### Board Settings ####
          self.brightness = brightness
     

     # set initial access token for user's spotify
     def set_spotify_access_token(self, access_token=None):
          if access_token == None:
               self.spotify_access_token = refresh_access_token(self.spotify_refresh_token)
          else:
               self.spotify_access_token = access_token

     # store and run periodic data collections from external apis 
     def api_data_container(self):
          while True:
               ################################# Api Data Collection Intervals #############################################################################################################################
               # Spotify = every 2 seconds                                                     # unkown            (limit)         # ~2 calls album/track_data       # if device on
               # Weather = every 10 minutes (time.sleep(400))    # 144 calls/day (avg)         # 1000 calls/day    (limit)         # ~1 call                         # if device on
               # Stock = every 10 minutes (time.sleep(400))      # 78 calls/day  (avg)         # 800 calls/day     (limit)         # 2 calls data/graph              # calls beteen 0930 and 1600
               #############################################################################################################################################################################################
               
               self.isDataReady = False

               # check to see if user has a weather api key
               try:
                    if self.data_interval % 400 == 0:
                         weather_data = get_weather(zip_code=self.zip_code, location_change=self.location_change, weather_data=self.api_data['weather'])
                         self.location_change = False

                         # check for valid zip code user input
                         if weather_data == 'invalid_zipcode' and self.channel =='weather':
                              self.channel = 'invalid_zipcode'
                         self.api_data["weather"] = weather_data # update display data
               except:
                    self.channel = "req_weather_api_key" if self.channel == 'weather' else self.channel
                    weather_data = None
                    self.api_data["weather"] = weather_data # update display data
                    print("openweathermap.org Api Key Required")
               
               # check to see if user has a twelve stock api key
               try:
                    if self.data_interval % 400 == 0:
                         is_market_sleeping = market_data_sleep_mode()

                         # skip api call if market closed and data already initially fetched
                         none_val = ['invalid_stock', 'req_stock_api_key', None]

                         if not is_market_sleeping or self.api_data["stock"] in none_val:
                              stock_data = package_stock_data(self.stock)
                              self.stock_change = False

                              # check for valid stock user input
                              if stock_data == 'invalid_stock' and self.channel == 'stock':
                                   self.channel = 'invalid_stock'
                              self.api_data["stock"] = stock_data # update display data
               except:
                    self.channel = "req_stock_api_key" if self.channel == 'stock' else self.channel
                    stock_data = None
                    self.api_data["stock"] = stock_data # update display data
                    print("twelvedata.com Api Key Required")
               
               # check to see if user is authenticated through iOS app
               try:
                    if self.data_interval % 8 == 0:
                         spotify_data = spotify_player(currently_playing, self.set_spotify_access_token ,self.spotify_access_token, self.spotify_refresh_token, 'currently_playing')
                         if spotify_data == 'timed_out':
                              spotify_data = self.api_data["spotify"]
                         elif spotify_data == 'no_device_active' and self.channel == 'spotify2': # handles in case of no song or device playing
                              self.channel = 'no_device_active'
                         self.api_data["spotify"] = spotify_data # update display data
                    else:
                         print(self.data_interval) # testing purposes to view interval
               except Exception as e:
                    self.channel = "req_spot_auth" if self.channel == 'spotify2' else self.channel
                    spotify_data = None
                    self.api_data["spotify"] = spotify_data # update display data
                    log_error_to_file(e)
                    print("Spotify Authentication Required", e)

                                   
               self.isDataReady = True

               self.data_interval -= 1
               
               if self.data_interval <= 0:
                    self.data_interval = 400
                    
               time.sleep(1)


     # update data store when input data changes
     def update_data_container(self):
          with self.lock:

               self.isDataReady = False
               
               # check to see if user has a weather api key
               try:
                    if self.location_change:
                         weather_data = get_weather(zip_code=self.zip_code, location_change=self.location_change, weather_data=self.api_data["weather"])
                         self.location_change = False
                         # check for valid zip code user input
                         if weather_data == 'invalid_zipcode' and self.channel =='weather' or self.channel =='invalid_zipcode':
                              self.channel = 'invalid_zipcode'
                         self.api_data["weather"] = weather_data # update display data
                    else:
                         print('zip code input did not change')
               except:
                    self.channel = "req_weather_api_key" if self.channel == 'weather' else self.channel
                    weather_data = None
                    self.api_data["weather"] = weather_data # update display data
                    print("openweathermap.org Api Key Required")
               
               # check to see if user has a twelve stock api key
               try:
                    if self.stock_change:
                         stock_data = package_stock_data(self.stock)
                         # check for valid stock user input
                         if stock_data == 'invalid_stock' and self.channel == 'stock' or self.channel == 'invalid_stock':
                              self.channel = 'invalid_stock'
                         self.api_data["stock"] = stock_data # update display data
                    else:
                         print('stock input did not change')
               except:
                    self.channel = "req_stock_api_key" if self.channel == 'stock' else self.channel
                    stock_data = None
                    self.api_data["stock"] = stock_data # update display data
                    print("twelvedata.com Api Key Required")

               # check to see if user is authenticated through iOS app
               try:
                    spotify_data = spotify_player(currently_playing, self.set_spotify_access_token ,self.spotify_access_token, self.spotify_refresh_token, 'currently_playing')
                    # handles in case of no song or device playing
                    if spotify_data == 'no_device_active' and self.channel == 'spotify2' or self.channel =='no_device_active': 
                         self.channel = 'no_device_active'
                    # changes view from req auth to spotify if token detected
                    elif self.channel == "req_spot_auth" and self.channel == 'spotify2' or self.channel =='req_spot_auth':
                         self.channel = "spotify2"
                    self.api_data["spotify"] = spotify_data # update display data
               except:
                    self.channel = "req_spot_auth" if self.channel == 'spotify2' else self.channel
                    spotify_data = None
                    self.api_data["spotify"] = spotify_data # update display data
                    print("Spotify Authentication Required")
                           
               
               self.isDataReady = True


     # init data collection for user
     def create_thread(self):
          if self.thread is None:
               # create user thread for personal api calls
               self.thread = Thread(target=self.api_data_container)
               self.thread.daemon = True
               self.thread.start()
               return jsonify(message="Data fetching started for user{}".format(self.client_id)), 204

          else:
               return jsonify(message="Thread already running for user{}".format(self.client_id)), 204
     

     # changes user parameters
     def update_thread(self, client_id:str, stock:str, zip_code:int, brightness:int):
          if self.thread != None:
               self.brightness = brightness

               # checks if location input has changed
               if self.zip_code != zip_code:
                    self.zip_code = zip_code
                    self.location_change = True 
               else:
                    self.location_change = False

               # checks if stock input has changed
               if self.stock != stock:
                    self.stock = stock
                    self.stock_change = True 
               else:
                    self.stock_change = False
               
               # this is called to ensure screen data updates before scheduled time
               self.update_data_container()

               return jsonify(message="Updated input data for user{}".format(client_id)), 204
          else:
               self.isDataUpdating = False
               return jsonify(message="no data available for this user"), 404
          

     # sets new channel of data for the user
     def update_channel(self, channel):
          if self.thread != None:
               try:
                    self.channel = channel
                    
               except Exception as e:
                    print(e)

               return jsonify(message="Updated channel data for user{}".format(self.client_id)), 204
          return jsonify(message="no data available for this user"), 404
     
     
