import time
from datetime import datetime
from rgbmatrix import graphics


class Clock_Stock_View:
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

        stockdata_font = graphics.Font()
        stockdata_font.LoadFont("Fonts/6x9.bdf")

        market_font = graphics.Font()
        market_font.LoadFont("Fonts/4x6.bdf")

      
        #colors
        white = graphics.Color(255, 255, 255)
        yellow = graphics.Color(252, 198, 3)
        red = graphics.Color(252, 0, 0)
        green = graphics.Color(0, 255, 0)
       
       
        # conditional rendering var
        loop_counter = 0
        isFirstLoop = True
        market_status_toggle = True
        day_month_toggle = True
        position = 64
        position_2 = None

        # release the http request
        self.user.displayLoaded = 'clock_stock'

        while True:
            self.main_canvas.Clear()

            # close view gracefully
            if self.user.channel != 'clock_stock':
                print('clock_stock loop terminated')
                return self.user.channel
            
            # check for valid api data
            if self.user.api_data['stock'] == None:
                self.user.channel = 'req_stock_api_key'
                break
            elif self.user.api_data['stock'] == 'invalid_stock':
                self.user.channel = 'invalid_stock'
                break
            
            # updating data
            ismarketOpen = self.user.api_data['stock']['is_market_open']
            ticker_symbol = self.user.api_data['stock']['stock_instance']['symbol']
            price_displayed = self.user.api_data['stock']['price_displayed']
            percent_change = self.user.api_data['stock']['stock_instance']['percent_change'] # want is as a raw str 
            price_change = self.user.api_data['stock']['price_change']

            # set stock colors
            if "-" in percent_change: 
                stock_color = red
                arrow_indicator = '\u25BC'
            elif float(percent_change) > 0: # set color if in the green
                stock_color = green
                arrow_indicator = '\u25B2'
            else:
                stock_color = white
                arrow_indicator = '--'

            # format display data
            percent_change = f"{float(percent_change):.2f}%"
            price_change = f"{float(price_change):.2f}"
            price_displayed = f"{float(price_displayed):.2f}"

            # time data
            date_data = datetime.now()
            current_time = date_data.strftime("%I:%M %p")
            day = date_data.strftime("%a").upper()
            month = date_data.strftime("%b").upper()
            date = date_data.strftime("%d")
            
            # positional parameters
            time_y = 10
            stock_y = 30
            

            # date position in code due to desired z plain
            if day_month_toggle:
                len_day = graphics.DrawText(self.main_canvas, date_font, 2, 18, yellow, day)
                graphics.DrawText(self.main_canvas, date_font, (len_day + 4), 18, yellow, date)
            else:
                len_month = graphics.DrawText(self.main_canvas, date_font, 2, 18, yellow, month)
                graphics.DrawText(self.main_canvas, date_font, (len_month + 4), 18, yellow, date)
            
            
            # -- time -- divided to correctly space numbers
            graphics.DrawText(self.main_canvas, time_font, 1, time_y, white, current_time[0])
            graphics.DrawText(self.main_canvas, time_font, 8, time_y, white, current_time[1])
            graphics.DrawText(self.main_canvas, time_font, 14, time_y, white, current_time[2])
            graphics.DrawText(self.main_canvas, time_font, 20, time_y, white, current_time[3])
            graphics.DrawText(self.main_canvas, time_font, 27, time_y, white, current_time[4])


            # market status
            if market_status_toggle:  
                graphics.DrawText(self.main_canvas, stockdata_font, 40, 8, white, "MRKT")
            else:                
                if ismarketOpen:
                    graphics.DrawText(self.main_canvas, stockdata_font, 40, 8, green, "OPEN")
                else:
                    graphics.DrawText(self.main_canvas, stockdata_font, 34, 8, red, "CLOSE")


            # bottom borders
            graphics.DrawLine(self.main_canvas, 0, 22, 63, 22, stock_color)
            graphics.DrawLine(self.main_canvas, 0, 31, 63, 31, stock_color)

            # stock data loop 1
            len_symb = graphics.DrawText(self.main_canvas, stockdata_font, position, stock_y, white, ticker_symbol)
            len_arrow = graphics.DrawText(self.main_canvas, stockdata_font, (position+len_symb + 3), stock_y, stock_color, arrow_indicator)
            len_price = graphics.DrawText(self.main_canvas, stockdata_font, (position+len_symb+len_arrow + 9), stock_y, stock_color, price_displayed)
            len_percent = graphics.DrawText(self.main_canvas, stockdata_font, (position+len_symb+len_price+len_arrow + 15), stock_y, white, percent_change)
            len_price_change = graphics.DrawText(self.main_canvas, stockdata_font, (position+len_symb+len_price+len_percent+len_arrow + 21), stock_y, stock_color, price_change)

            # positional mapping loop 1
            len_dataLoop_1 = position+len_symb+len_arrow+len_price+len_percent+len_price_change + 27
            
            # set data loop 2 initia position
            if isFirstLoop:
                isFirstLoop = False
                position_2 = len_dataLoop_1
                print(position_2)

            # stock data loop 2
            len_symb_2 = graphics.DrawText(self.main_canvas, stockdata_font, position_2, stock_y, white, ticker_symbol)
            len_arrow_2 = graphics.DrawText(self.main_canvas, stockdata_font, (position_2+len_symb_2 + 3), stock_y, stock_color, arrow_indicator)
            len_price_2 = graphics.DrawText(self.main_canvas, stockdata_font, (position_2+len_symb_2+len_arrow_2 + 9), stock_y, stock_color, price_displayed)
            len_percent_2 = graphics.DrawText(self.main_canvas, stockdata_font, (position_2+len_symb_2+len_price_2+len_arrow_2 + 15), stock_y, white, percent_change)
            len_price_change_2 = graphics.DrawText(self.main_canvas, stockdata_font, (position_2+len_symb_2+len_price_2+len_percent_2+len_arrow_2 + 21), stock_y, stock_color, price_change)

            # positional mapping loop 2
            len_dataLoop_2 = position_2+len_symb_2+len_arrow_2+len_price_2+len_percent_2+len_price_change_2

            # toggle "MRKT" / "Open Status"
            if loop_counter % 15 == 0:
                market_status_toggle = not market_status_toggle

            # data loop 1 reset
            if (len_dataLoop_1 < -3 ): # -3 is the offset 
                loop_counter = 0
                position = len_dataLoop_2 + 27
                day_month_toggle = not day_month_toggle
            
            # data loop 2 reset
            if (len_dataLoop_2 < -27 ): # -27 is the offset 
                loop_counter = 0
                position_2 = len_dataLoop_1 
                day_month_toggle = not day_month_toggle

            # increment loop variabels
            position -= 1
            position_2 -= 1
            loop_counter += 1

            time.sleep(0.15)

            self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)
            

            

