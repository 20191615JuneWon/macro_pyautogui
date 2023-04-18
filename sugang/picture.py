import pyautogui
import time
import keyboard

class PictureMaker:
    def __init__(self):
        self.position = pyautogui.locateOnScreen('naver.png', confidence=0.8)

    def getPNG(self):
        return self.position

    #     while True:
    #         if keyboard.is_pressed('space'):
    #             pyautogui.screenshot('target.png')
    #             print('사진촬영완료')
    #             return


if __name__ == '__main__':
    s = PictureMaker()
    print(s.position)
