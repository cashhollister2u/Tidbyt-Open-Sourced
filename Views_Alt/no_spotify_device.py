import time
from rgbmatrix import graphics


class No_Spotify_Device:
    def __init__(self, user, display):
        self.user = user # display data
        self.options = display.options # display settings
        self.matrix = display.matrix # init display 
        self.main_canvas = display.main_canvas

        

    def run(self):
        
        # fonts
        title_font = graphics.Font()
        title_font.LoadFont("Fonts/4x6.bdf")

        # colors
        white = graphics.Color(255, 255, 255)
        gray = graphics.Color(50,50,50)
        black = graphics.Color(0, 0, 0)

        # rendering variables
        isScrolling = True
        position = 2

        # release the http request
        self.user.displayLoaded = 'no_device_active'

        while True:
            self.main_canvas.Clear()

            # close view gracefully
            if self.user.channel != 'no_device_active':
                print('no_device_active loop terminated')
                return self.user.channel
            
            # check if api data was updated 
            if self.user.api_data['spotify'] != None and self.user.api_data['spotify'] != 'no_device_active':
                self.user.channel = 'spotify2'
                break

            
            # Title text
            len_title = graphics.DrawText(self.main_canvas, title_font, position, 9, white, "No Song/Device Found")
            
            if len_title < 32:
                isScrolling = False
                position = (32 - len_title) // 2
            else:
                isScrolling = True

       
            # pause button
            for num in range(12, 20):
                if num == 15 or num == 16:
                    pass
                else:
                    graphics.DrawLine(self.main_canvas, num, 13, num, 21, white)
            

            # progress bar
            left_bound = 4
            right_bound = 28
            progress_y = 26
            
            graphics.DrawLine(self.main_canvas, left_bound, progress_y, right_bound, progress_y, gray) # percent left of song

            # empty album frame
            graphics.DrawLine(self.main_canvas, 32, 0, 63, 0, white) # top
            graphics.DrawLine(self.main_canvas, 32, 1, 32, 31, white) # left
            graphics.DrawLine(self.main_canvas, 63, 1, 63, 31, white) # right
            graphics.DrawLine(self.main_canvas, 33, 31, 62, 31, white) # bottom

            # black cube album cover substitute
            for num in range(33,63):
                graphics.DrawLine(self.main_canvas, num, 1, num, 30, black)

            # black lines to hide text overflow
            graphics.DrawLine(self.main_canvas, 0, 0, 0, 31, black)
            graphics.DrawLine(self.main_canvas, 1, 0, 1, 31, black)
            graphics.DrawLine(self.main_canvas, 30, 0, 30, 31, black)
            graphics.DrawLine(self.main_canvas, 31, 0, 31, 31, black)

            # pause the title when at start and display fully rendered
            if position == 1:
                time.sleep(3)
            
            if isScrolling:
                position -=1
            
            if (position + len_title <= 0):
                position = 2

            # rate of text scroll
            time.sleep(0.15)

            self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)

            

            

            

