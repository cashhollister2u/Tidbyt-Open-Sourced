import time
from rgbmatrix import graphics


class Stock_Api_key:
    def __init__(self, user, display):
        self.user = user # display data
        self.options = display.options # display settings
        self.matrix = display.matrix # init display 
        self.main_canvas = display.main_canvas
        

    def run(self):

        # fonts
        font = graphics.Font()
        font.LoadFont("Fonts/6x12.bdf")

        # colors
        white = graphics.Color(255, 255, 255)

        # positional rendering
        position = 2

        # release the http request
        self.user.displayLoaded = 'req_stock_api_key'
        while True:
            self.main_canvas.Clear()

            # close view gracefully
            if self.user.channel != 'req_stock_api_key':
                print('Twelve api required loop terminated')
                return self.user.channel
            
            len_text = graphics.DrawText(self.main_canvas, font, position, 16, white, "Add twelvedata.com api key to Secrets/api_keys.py")
            
            if (position + len_text <= 0):
                position = 2

            position -= 1

            time.sleep(0.05)

            self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)
            

            

