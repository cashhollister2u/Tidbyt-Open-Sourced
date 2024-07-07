import time
from rgbmatrix import graphics


class Invalid_Zip_Code:
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
        self.user.displayLoaded = 'invalid_zipcode'

        while True:
            self.main_canvas.Clear()

            # close view gracefully
            if self.user.channel != 'invalid_zipcode':
                print('invalid_zipcode loop terminated')
                return self.user.channel
            
            # check if api data was updated 
            if self.user.api_data['weather'] != None and self.user.api_data['weather'] != 'invalid_zipcode':
                self.user.channel = 'weather'
                break

            len_text = graphics.DrawText(self.main_canvas, font, position, 16, white, "Invalid Zip Code")
            
            if (position + len_text <= 0):
                position = 2

            position -= 1

            time.sleep(0.05)

            self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)
            

            

