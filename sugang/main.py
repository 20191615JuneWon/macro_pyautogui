import tkinter
import finder
import time

if time.localtime().tm_hour == 10:

    finder.PositionValue.mouse_position()

window = tkinter.Tk()
window.title("Sugang controller")

# window.geometry("500x300+100+100")



window.mainloop()
