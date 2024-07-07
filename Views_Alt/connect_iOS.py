import time
from rgbmatrix import graphics


class Connect_IOS:
    def __init__(self, shared_user, display):
        self.shared_user = shared_user
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

            # close view gracefully
            if self.shared_user.get_user() != None:
                print('connect to ios loop terminated' ,self.shared_user.get_user())
                return self.shared_user.get_user()
            

            len_text = graphics.DrawText(self.main_canvas, font, position, 16, white, "Connect via iOS app")
            
            if (position + len_text <= 0):
                position = 2

            position -= 1

            time.sleep(0.05)

            self.main_canvas = self.matrix.SwapOnVSync(self.main_canvas)
            

            

