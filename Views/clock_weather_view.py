import time
from datetime import datetime
from rgbmatrix import graphics
from PIL import Image


class Clock_Weather_View:
    def __init__(self, user, display):
        self.user = user # display data
        self.options = display.options # display settings
        self.matrix = display.matrix # init display 
        self.main_canvas = display.main_canvas
        

    def run(self):

        # fonts
        time_font = graphics.Font()
        time_font.LoadFont("Fonts/6x13B.bdf")

        date_font = graphics.Font()
        date_font.LoadFont("Fonts/6x12.bdf")

        week_day_font = graphics.Font()
        week_day_font.LoadFont("Fonts/6x9.bdf")

        temp_font = graphics.Font()
        temp_font.LoadFont("Fonts/MatrixChunky6X.bdf")

        # colors
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252, 198, 3)
        red = graphics.Color(252, 0, 0)
        purple = graphics.Color(235, 52, 235)

        # image paths
        cloudy = "Pictures/cloudy.bmp"
        rainy = "Pictures/rainy.bmp"
        lightning = "Pictures/lightning.bmp"
        snowy = "Pictures/snowy.bmp"

        # release the http request
        self.user.displayLoaded = 'weather'
        
        while True:
            self.main_canvas.Clear()

            # close view gracefully
            if self.user.channel != 'weather':
                print('weather loop terminated')
                return self.user.channel
            
            # check for valid api data
            if self.user.api_data['weather'] == None:
                self.user.channel = 'req_weather_api_key'
                break
            elif self.user.api_data['weather'] == 'invalid_zipcode':
                    self.user.channel = 'invalid_zipcode'
                    break

            # updating data
            temp = self.user.api_data['weather']['temp']
            weather_code = str(self.user.api_data['weather']['weather_code']) 

             # Based on code set the weather icon to be displayed
            if weather_code[0] == '2':
                weather_path = lightning
            if weather_code[0] == '3' or weather_code[0] == '5':
                weather_path = rainy
            if weather_code[0] == '6':
                weather_path = snowy
            if weather_code[0] == '7' or weather_code[0] == '8':
                weather_path = cloudy               

            date_data = datetime.now()
            current_time = date_data.strftime("%I:%M %p")
            day = date_data.strftime("%a").upper()
            month = date_data.strftime("%b").upper()
            date = date_data.strftime("%d")
            time_y = 10

            
            # -- time -- divided to correctly space numbers
            graphics.DrawText(self.main_canvas, time_font, 1, time_y, white, current_time[0])
            graphics.DrawText(self.main_canvas, time_font, 8, time_y, white, current_time[1])
            graphics.DrawText(self.main_canvas, time_font, 14, time_y, white, current_time[2])
            graphics.DrawText(self.main_canvas, time_font, 20, time_y, white, current_time[3])
            graphics.DrawText(self.main_canvas, time_font, 27, time_y, white, current_time[4])

            # date position in code due to desired z plain
            len_month = graphics.DrawText(self.main_canvas, date_font, 2, 19, yellow, month)
            graphics.DrawText(self.main_canvas, date_font, (len_month + 4), 19, yellow, date)

            graphics.DrawText(self.main_canvas, week_day_font, 16, 31, purple, day)

            # divide
            graphics.DrawLine(self.main_canvas, 34, 1, 34, 31, red)

            # temp
            len_temp = graphics.DrawText(self.main_canvas, temp_font, 37, 30, yellow, f"{temp:.1f}")
            graphics.DrawCircle(self.main_canvas, 38 + len_temp, 25, 1, yellow)


            

            self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)

            # weather image
            # Display the image if available
            if weather_path:
                image = Image.open(weather_path)
                self.matrix.SetImage(image, 36, 1)
            
            time.sleep(4)
            

