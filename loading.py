import time
from rgbmatrix import graphics
from rgbmatrix import RGBMatrix, RGBMatrixOptions


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

class Connect_IOS:
    def __init__(self, display):
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

        while True:
            self.main_canvas.Clear()

           
            

            len_text = graphics.DrawText(self.main_canvas, font, position, 16, white, "Loading...")
            
            if (position + len_text <= 0):
                position = 10

         

            time.sleep(0.05)

            self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)
            

            
display = Generate_Display()
run = Connect_IOS(display=display)
run.run()
