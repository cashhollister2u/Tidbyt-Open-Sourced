from rgbmatrix import RGBMatrix, RGBMatrixOptions, graphics
import time
import gc

# custom views
from Views.spotify_2_view import Spotify_2_View
from Views.stock_view import StockView
from Views.clock_stock_view import Clock_Stock_View
from Views.clock_weather_view import Clock_Weather_View

# alt views
from Views_Alt.connect_iOS import Connect_IOS
from Views_Alt.req_spotify_auth import Spotify_Auth
from Views_Alt.no_spotify_device import No_Spotify_Device
from Views_Alt.req_stock_key import Stock_Api_key
from Views_Alt.invalid_stock_input import Invalid_Stock
from Views_Alt.req_weather_key import Weather_Api_key
from Views_Alt.invalid_zipcode import Invalid_Zip_Code

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


def display_loop(user, shared_user):   

    display = Generate_Display()
    
    # main loop
    while True:
        
        if user == None:     
            #user = shared_user.get_user()
            run_connect_ios_view = Connect_IOS(shared_user=shared_user, display=display)
            user = run_connect_ios_view.run()

        else:
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
                    print('before weather class')
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