import time
from rgbmatrix import graphics
import math


class Spotify_2_View:
    def __init__(self, user, display):
        self.user = user # display data
        self.options = display.options # display settings
        self.matrix = display.matrix # init display 
        self.main_canvas = display.main_canvas
        self.position = 3
        self.title = None
        self.stable_mode = True # change to false to scroll text w/ flicker

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
        position = 3

        # release the http request
        self.user.displayLoaded = 'spotify2'
       
        first_loop = True # conditional flag

        while True:
            # clear each loop if not stable mode
            if not self.stable_mode:
                self.main_canvas.Clear()
           
            try: 
                # updating data
                title = self.user.api_data['spotify']['name']
                is_playing = self.user.api_data['spotify']['is_playing']
                duration = self.user.api_data['spotify']['duration']
                progress = self.user.api_data['spotify']['progress']
                image_data = self.user.api_data['spotify']['album_cover']

                # clear canvas when song changes
                if self.title != title:
                    print(title, self.title)
                    self.title = title
                    self.main_canvas.Clear()
            except:
                self.user.channel = 'no_device_active'
        

            # close view gracefully
            if self.user.channel != 'spotify2':
                self.main_canvas.Clear()
                print('spotify loop terminated')
                return self.user.channel
            
            # check for valid api data
            if self.user.api_data['spotify'] == None:
                self.user.channel = 'req_spot_auth'
                break
            elif self.user.api_data['spotify'] == 'no_device_active':
                self.user.channel = 'no_device_active'
                break
            
            # calculate position for title in stable mode
            if self.stable_mode:
                self.main_canvas.Clear()
                title = title[:7]
                position = math.ceil((31 - (len(title) * 4)) / 2)

            # Title text
            len_title = graphics.DrawText(self.main_canvas, title_font, position, 9, white, title)

            # pause / play buttons
            if is_playing:
                # pause button
                for num in range(12, 20):
                    if num == 15 or num == 16:
                        pass
                    else:
                        graphics.DrawLine(self.main_canvas, num, 13, num, 21, white)
            else:
                # play button
                for index, num in enumerate(range(14, 19)):
                    upper_limit = (13 + index)
                    lower_limit = (21 - index)
                    graphics.DrawLine(self.main_canvas, num, upper_limit, num, lower_limit, white)

            # progress bar
            left_bound = 3
            right_bound = 28
            progress_y = 26
            percent_progress = progress / duration
            completed = int(percent_progress * 26)
            remaining = (26 - completed) - 1
            graphics.DrawLine(self.main_canvas, (right_bound - remaining), progress_y, right_bound, progress_y, gray) # percent left of song
            graphics.DrawLine(self.main_canvas, left_bound, progress_y, (completed + left_bound), progress_y, white) # percent into song
            

            # black lines to hide text overflow
            graphics.DrawLine(self.main_canvas, 0, 0, 0, 31, black)
            graphics.DrawLine(self.main_canvas, 1, 0, 1, 31, black)
            graphics.DrawLine(self.main_canvas, 30, 0, 30, 31, black)
            graphics.DrawLine(self.main_canvas, 31, 0, 31, 31, black)

            # positional changes when not in stable mode and album cover 
            if not self.stable_mode:
                # album Cover
                self.matrix.SetImage(image_data.convert('RGB'), 32, 0) # must come after canvas creation 

                if len_title < 32:
                    isScrolling = False
                    position = (32 - len_title) // 2
                    self.main_canvas.Clear()
                else:
                    isScrolling = True

                # pause the title when at start and display fully rendered
                if position == 2:
                    time.sleep(5)
                
                if isScrolling:
                    position -=1
                
                if (position + len_title <= 0):
                    position = 3

            # display text
            self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)

            
            # rate of text scroll and album cover 
            if self.stable_mode and first_loop:
                # album Cover
                self.matrix.SetImage(image_data.convert('RGB'), 32, 0) # must come after canvas creation 
                time.sleep(.15)
                self.main_canvas.Clear()
                first_loop = False
            elif self.stable_mode:
                # album Cover
                self.matrix.SetImage(image_data.convert('RGB'), 32, 0) # must come after canvas creation 
                time.sleep(4)
            else:
                time.sleep(.15)

            

            

            

