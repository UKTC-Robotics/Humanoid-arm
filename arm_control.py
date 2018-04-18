import tkinter as tk

import serial
import time
states = []

msg = 'abcde\n'
arm = serial.Serial('com8', 9600)

#START OBUCHENIE
def start():
    global states
    states = []

def remember():
    global states
    global msg
    states.append(msg)


def play():
    global states
    for op in states :
        arm.write(op.encode())
        time.sleep(sld.get())

def thumb():
    global msg
    if msg[0] == 'A':
        msg = msg.replace('A', 'a')
    else:
        msg= msg.replace('a', 'A')

    #ZABRANA NA thumb+MIDDLE
    if msg != 'abCde:' :
        arm.write(msg.encode())
    else:
        print('error')


def  index():
    global msg
    if msg[1] == 'B':
        msg =  msg.replace('B', 'b')
    else:
        msg = msg.replace('b', 'B')
    arm.write(msg.encode())

def middle():
    global msg
    if msg[2] == 'C':
        msg = msg.replace('C', 'c')
    else:
        msg = msg.replace('c', 'C')
    arm.write(msg.encode())

def ring():
    global msg
    if msg[3] == 'D':
        msg = msg.replace('D', 'd')
    else:
        msg = msg.replace('d', 'D')
    arm.write(msg.encode())

def baby():
    global msg
    if msg[4] == 'E':
        msg = msg.replace('E', 'e')
    else:
     msg = msg.replace('e', 'E')
    arm.write(msg.encode())


 #pravi //
gui = tk.Tk ()

gui.geometry("400x600")

#prusti
palec = tk.Button (gui, text='THUMB', bg = 'lightpink', command=thumb, height= 2, padx= 9 )
palec.place (x= 10, y= 110)

pokazalec = tk.Button(gui, text='INDEX  ', bg = 'lightpink', command=index , height= 2, padx= 9)
pokazalec.place (x=90, y= 110)

sreden = tk.Button (gui, text='MIDDLE', bg = 'lightpink', command=middle , height= 2, padx= 7)
sreden.place (x=170, y= 110)

bezimen = tk.Button (gui, text='RING', bg ='lightpink', command=ring , height= 2, padx= 12)
bezimen.place (x=250, y= 110)

kutre = tk.Button (gui, text='BABY ', bg = 'lightpink', command= baby  ,height= 2, padx= 12)
kutre.place (x=320, y= 110)

# opravlenie
clear = tk.Button (gui, text='START ', bg = 'cyan', command= start  ,height= 2, padx= 9  )
clear.place (x=70, y=280)

remember= tk.Button (gui, text='REMEMBER ', bg = 'cyan', command= remember ,height= 2, padx= 2 )
remember.place (x=165, y= 280)

playb = tk.Button(gui, text='REPEAT', bg = 'cyan' , command=play , height= 2 , padx=9 )
playb.place(x=270, y=280)

#slider
sld = tk.Scale(gui,from_=1, to=5  , orient= tk.HORIZONTAL)
sld.place(x= 150, y=430 )

#tekst
texts = tk.Label(gui, text= 'CONTROL FINGERS' ,  foreground="black"  )
texts.config( font=('times', 24, 'italic'  ))
texts.place (x=60, y= 30)

hd = tk.Label(gui, text= 'ARM LEARNING' ,  foreground="black" )
hd.config (font=('times', 24, 'italic'))
hd.place (x=90, y= 200)

textss = tk.Label(gui, text= 'SPEED' ,  foreground="black" )
textss.config( font=('times', 24, 'italic'))
textss.place (x=150, y= 360)

textsl = tk.Label(gui, text= 'Stefani Mincheva 2018' ,  foreground="black" )
textsl.config(  font=('times', 16, 'italic'))
textsl.place (x=195, y= 570)

gui.mainloop()
