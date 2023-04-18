import pyautogui
import time
import picture
import keyboard

# important thing i think, abs value of position, without abs position, need to calculate exact position,
# need to measure yourself.


class PositionValue:
    def __init__(self):
        self.p = picture.PictureMaker()


    def position_handler(self):
        position = self.p.getPNG()
        print(position)
        pyautogui.moveTo(position[0], position[1])
        pyautogui.doubleClick()


    def check_mouse(self): # debug
        while True:
            if keyboard.is_pressed('space'):
                return
            time.sleep(1)
            print(pyautogui.position())


if __name__ == '__main__':
    s = PositionValue()
    s.position_handler()
    # s.check_mouse()
    print(s)