from tkinter import Tk, Canvas, PhotoImage, Label
import time
import os
import sys
import random
import threading
from multiprocessing import Process, current_process

game = Tk()

canvas = Canvas(game, width=1500, height=1500, bg="green")
canvas.pack()



frame1 = PhotoImage(file="frame1.png")
frame2 = PhotoImage(file="frame2.png")
frame3 = PhotoImage(file="frame3.png")
frame4 = PhotoImage(file="frame4.png")
frame5 = PhotoImage(file="frame5.png")
frame6 = PhotoImage(file="frame6.png")
frame7 = PhotoImage(file="frame7.png")
frame8 = PhotoImage(file="frame8.png")
frame9 = PhotoImage(file="frame9.png")
frame10 = PhotoImage(file="frame10.png")
frame11 = PhotoImage(file="frame11.png")
frame12 = PhotoImage(file="frame12.png")
frame13 = PhotoImage(file="frame13.png")
frame14 = PhotoImage(file="frame14.png")
frame15 = PhotoImage(file="frame15.png")
frame16 = PhotoImage(file="frame16.png")
frame17 = PhotoImage(file="frame17.png")


gifpics = [frame1, frame2, frame3, frame4, frame5, frame6, frame7, frame8,
 frame9, frame10, frame11, frame12, frame13, frame14, frame15, frame16, frame17]


x = random.randint(1, 1500)
y = 0

new = []

def zombiespawn():
    while True:
        x = random.randint(1, 1500)
        y = 0
        while True:
                for i in gifpics:
                    frame = canvas.create_image(x, y, image=i)
                    time.sleep(0.05)
                    x = x
                    y = y+5
                    newcoords = canvas.coords(frame)
                    game.update()
                    canvas.delete(frame)
                    if newcoords[1] == 1000:
                        break
                if newcoords[1] == 1000:
                    break
        if newcoords[1] == 1000:
            break

numberOfThreads = random.randint(1,6)

listThreads = []

# for i in range(numberOfThreads):
t1 = threading.Thread(target=zombiespawn)
t2 = threading.Thread(target=zombiespawn)



t1.start()
game.after(1000, t2.start())




game.mainloop()
