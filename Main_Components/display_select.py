from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import gc
import json

# custom views
from Views.spotify_2_view import Spotify_2_View
from Views.stock_view import StockView
from Views.clock_stock_view import Clock_Stock_View
from Views.clock_weather_view import Clock_Weather_View

# alt views
from Views_Alt.req_spotify_auth import Spotify_Auth
from Views_Alt.no_spotify_device import No_Spotify_Device
from Views_Alt.req_stock_key import Stock_Api_key
from Views_Alt.invalid_stock_input import Invalid_Stock
from Views_Alt.req_weather_key import Weather_Api_key
from Views_Alt.invalid_zipcode import Invalid_Zip_Code

# User Class
from Main_Components.user_data import User

### IMPORTANT : Must delete and call garbage collector on the current display before switching to a new dislay 
###             otherwise function will crash very baddly                                                     
###     
### In Case of Bad Crash : Call "ps aux | grep main.py" then "sudo kill <the number to the right of daemon>"


class Generate_Display():
        def __init__(self, brightness=100, **kwargs):
            # Initialize the matrix configuration
            self.options = RGBMatrixOptions()
            self.options.rows = kwargs.get('led_rows', 32)
            self.options.cols = kwargs.get('led_cols', 64)
            self.drop_privileges = False
            self.options.chain_length = kwargs.get('led_chain', 1)
            self.options.parallel = kwargs.get('led_parallel', 1)
            self.options.brightness = kwargs.get('led_brightness', brightness)
            self.options.gpio_slowdown = kwargs.get('led_slowdown_gpio', 4)
            self.matrix = RGBMatrix(options=self.options)
            self.main_canvas = self.matrix.CreateFrameCanvas()

def create_user():
    with open("Secrets/user_inputs.json", "r") as file:
        data = json.load(file)
    
    zip_code = data.get("zip_code") if data.get("zip_code") else None
    stock = data.get("stock") if data.get("stock") else None
    channel = data.get("channel") if data.get("channel") else None

    try:
        # access refresh token saved to .json file
        with open("Secrets/spotify_refresh_token.json", 'r') as file:
            refresh_token = json.load(file)
            refresh_token = refresh_token['refresh_token']
    except:
        refresh_token = None

    return User(client_id='cc3c15a0cadf9c', stock=stock, zip_code=zip_code, spotify_refresh_token=refresh_token, channel=channel)


def display_loop(shared_user):   

    display = Generate_Display()
    
    user = create_user()
    user.set_spotify_access_token()
    user.create_thread_Not_Flask()
    # pass user to main after created
    shared_user.set_user(user)

    # main loop
    while True:
        if user:
            # main views
            if user.channel == "clock_stock":
                if user.isDataReady:
                    run_clock_stock_view = Clock_Stock_View(user=user, display=display)
                    run_clock_stock_view.run()
                    
                    # clean up display 
                    del run_clock_stock_view
                    gc.collect()
                
                
            elif user.channel == "stock":
                if user.isDataReady:
                    run_stock_view = StockView(user=user, display=display)
                    run_stock_view.run()
                    
                    # clean up display 
                    del run_stock_view
                    gc.collect()
                
                
            elif user.channel == "spotify2":
                if user.isDataReady:
                    run_spotify_2_view = Spotify_2_View(user=user, display=display)
                    run_spotify_2_view.run()
                    
                    # clean up display 
                    del run_spotify_2_view
                    gc.collect()
                    
                        
            elif user.channel == "weather":
                if user.isDataReady:
                    run_clock_view = Clock_Weather_View(user=user, display=display)
                    run_clock_view.run()
                    
                    # clean up display 
                    del run_clock_view
                    gc.collect()
                
            
            # alt views
            elif user.channel == "req_spot_auth":
                if user.isDataReady:
                    run_spotify_altview = Spotify_Auth(user=user, display=display)
                    run_spotify_altview.run()
                    
                    del run_spotify_altview
                    gc.collect()


            elif user.channel == "no_device_active": # spotify alt view
                if user.isDataReady:
                    run_noDevice_altview = No_Spotify_Device(user=user, display=display)
                    run_noDevice_altview.run()
                    
                    del run_noDevice_altview
                    gc.collect()


            elif user.channel == "req_stock_api_key":
                if user.isDataReady:
                    run_stock_altview = Stock_Api_key(user=user, display=display)
                    run_stock_altview.run()
                    
                    del run_stock_altview
                    gc.collect()


            elif user.channel == "invalid_stock":
                if user.isDataReady:
                    run_invalid_stock_altview = Invalid_Stock(user=user, display=display)
                    run_invalid_stock_altview.run()
                    
                    del run_invalid_stock_altview
                    gc.collect()


            elif user.channel == "req_weather_api_key":
                if user.isDataReady:
                    run_weather_altview = Weather_Api_key(user=user, display=display)
                    run_weather_altview.run()
                    
                    del run_weather_altview
                    gc.collect()


            elif user.channel == "invalid_zipcode":
                if user.isDataReady:
                    run_invalid_zipcode_altview = Invalid_Zip_Code(user=user, display=display)
                    run_invalid_zipcode_altview.run()
                    
                    del run_invalid_zipcode_altview
                    gc.collect()
        
    
        time.sleep(1)