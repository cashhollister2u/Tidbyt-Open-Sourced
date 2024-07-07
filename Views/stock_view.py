import time
import math
from rgbmatrix import graphics


class StockView:
    def __init__(self, user, display):
        self.user = user # display data
        self.options = display.options # display settings
        self.matrix = display.matrix # init display 
        self.main_canvas = display.main_canvas
        

    def run(self):
            
            # fonts 
            font = graphics.Font()
            font.LoadFont("Fonts/MatrixChunky6X.bdf")

            #colors
            red = graphics.Color(255, 0, 0)
            green = graphics.Color(0, 255, 0)
            white = graphics.Color(255, 255, 255)

            # release the http request
            self.user.displayLoaded = 'stock'

            while True:
                self.main_canvas.Clear()
                
                # close view gracefully
                if self.user.channel != 'stock':
                    print('stock loop terminated')
                    return self.user.channel
                
                # check for valid api data
                if self.user.api_data['stock'] == None:
                    self.user.channel = 'req_stock_api_key'
                    break
                elif self.user.api_data['stock'] == 'invalid_stock':
                    self.user.channel = 'invalid_stock'
                    break

                # updating data
                stock_instance = self.user.api_data['stock']['stock_instance']
                stockGraphData = self.user.api_data['stock']['stockGraphData']
                triangle_x_offset = self.user.api_data['stock']['triangle_x_offset']
                price_displayed = self.user.api_data['stock']['price_displayed']
                price_change_len = self.user.api_data['stock']['price_change_len']
                price_change = self.user.api_data['stock']['price_change']
                percent_change_len = self.user.api_data['stock']['percent_change_len']
                percent_change = self.user.api_data['stock']['percent_change']
                x_axis_height = self.user.api_data['stock']['x_axis_height']
                high_unit_measurement = self.user.api_data['stock']['high_unit_measurement']
                low_unit_measurement = self.user.api_data['stock']['low_unit_measurement']


                # set color for non graph display objects / create said display objects 
                if "-" in stock_instance['percent_change']: # set color if in the red
                    text_color = red
                    # Display indicator triangle
                    graphics.DrawLine(self.main_canvas, triangle_x_offset, 2, triangle_x_offset+4, 2, text_color) # triangle layer   
                    graphics.DrawLine(self.main_canvas, triangle_x_offset+1, 3, triangle_x_offset+3, 3, text_color) # triangle layer                 
                    graphics.DrawLine(self.main_canvas, triangle_x_offset+2, 4, triangle_x_offset+2, 4, text_color) # triangle layer     
                    
                elif float(stock_instance['percent_change']) > 0: # set color if in the green
                    text_color = green
                    # Display indicator triangle
                    graphics.DrawLine(self.main_canvas, triangle_x_offset+2, 2, triangle_x_offset+2, 2, text_color) # triangle layer   
                    graphics.DrawLine(self.main_canvas, triangle_x_offset+1, 3, triangle_x_offset+3, 3, text_color) # triangle layer                 
                    graphics.DrawLine(self.main_canvas, triangle_x_offset, 4, triangle_x_offset+4, 4, text_color) # triangle layer     

                    
                else: # white if neutral day
                    text_color = white
                    # Display indicator triangle
                    graphics.DrawLine(self.main_canvas, triangle_x_offset, 3, triangle_x_offset+4, 3, white) # neutral line                
                
                
                # Display ticker
                graphics.DrawText(self.main_canvas, font, 1, 7, white, stock_instance['symbol'])
                # Display price
                graphics.DrawText(self.main_canvas, font, 2, 14, white, f"{price_displayed:.2f}")

                # Display Price Difference 
                priceD_xValue = 52 - (((price_change_len - 1)*3) + (price_change_len - 4))
                graphics.DrawText(self.main_canvas, font, priceD_xValue, 7, text_color, f"{price_change:.2f}")

                # Display Percent Difference 
                percentD_xValue = 52 - (((percent_change_len - 1)*3) + (percent_change_len - 4))
                graphics.DrawText(self.main_canvas, font, percentD_xValue, 14, text_color, f"{percent_change:.2f}")
                
                # create custom display for percent sign
                graphics.DrawLine(self.main_canvas, 57,9,57,9, text_color) # dot
                graphics.DrawLine(self.main_canvas, 61,13,61,13, text_color) # dot
                graphics.DrawLine(self.main_canvas, 61,9,57,13, text_color) # slash


                # append the graph lines to the group using for loop
                for index, quote in enumerate(stockGraphData):
                    # checks if negative line
                    if (quote['close']) < (stock_instance['previous_close']):
                        # assign line length based on ratio to day low, unit of measurement, and relative location of x axis 
                        end_point = x_axis_height + (math.ceil((float(stock_instance['previous_close']) - float(quote['close'])) / low_unit_measurement))
                        # Display the 1/64 lines on graph
                        graphics.DrawLine(self.main_canvas, index, x_axis_height, index, end_point - 1, red)
                        
                        # Display graph outline
                        graphics.DrawLine(self.main_canvas, index, end_point, index, end_point, white) # dot
                        
                    # checks if positive line
                    elif (quote['close']) > (stock_instance['previous_close']):
                        # assign line length based on ratio to day high, unit of measurement, and relative location of x axis 
                        end_point = x_axis_height - (math.ceil((float(quote['close']) - float(stock_instance['previous_close'])) / high_unit_measurement))
                        # Display the 1/64 lines on graph
                        graphics.DrawLine(self.main_canvas, index, x_axis_height, index, end_point + 1, green)
                        # Display graph outline
                        graphics.DrawLine(self.main_canvas, index, end_point, index, end_point, white) # dot

                    # if neutral sets pixel on x axis
                    else:
                        # Display if quote is same as x axis
                        graphics.DrawLine(self.main_canvas, index, x_axis_height, index, x_axis_height, white) # dot

                # rate of text scroll
                time.sleep(4)

                self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)