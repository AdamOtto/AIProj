from tkinter import *
from PIL import Image, ImageDraw
import os
import numpy as np
import AI

def updateMouseLoc(event):
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
    canvas.old_coords = x, y

def clearCanvas(event):
    global imgDupe, image1
    canvas.delete("all")
    image1 = Image.new("RGB", (width, height), (255, 255, 255))
    imgDupe = ImageDraw.Draw(image1)

def getImagePath():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(dir_path + "\\images")
    return dir_path + "\\images"

def saveImage(filename, image):
    newImg = image.resize((28, 28),resample = Image.NEAREST)
    newImg.save(getImagePath() + "\\" + filename)

def draw(event):
    global imgDupe
    x, y = event.x, event.y
    if canvas.old_coords:
        x1, y1 = canvas.old_coords
        canvas.create_line(x, y, x1, y1, width=8)
        imgDupe.line((x,y,x1,y1), fill=0, width=8)
        #print("x: " + str(x) + ", y: " + str(y) + ", x1: " + str(x1) + ", y1: " + str(y1))
    canvas.old_coords = x, y

def testNumber():
    global image1
    newImg = image1.resize((28, 28),resample = Image.NEAREST )
    dataInput = convArrayToMatrix(np.array(newImg))
    temp = np.expand_dims(dataInput, axis=0)
    updateLabels(AI.predict(temp))

    return True


def convArrayToMatrix(ar):
    retVal = np.zeros((28,28))
    for x in range(0, 28):
        temp = np.zeros(28)
        for y in range(0, 28):
            avg = sum(ar[x,y])
            avg = avg / 3
            temp[y] = 1.0 - (avg / 255)
        retVal[x] = temp
    return retVal

def updateLabels(values):
    l0.set("0: " + "%.3f" % values[0, 0])
    l1.set("1: " + "%.3f" % values[0, 1])
    l2.set("2: " + "%.3f" % values[0, 2])
    l3.set("3: " + "%.3f" % values[0, 3])
    l4.set("4: " + "%.3f" % values[0, 4])
    l5.set("5: " + "%.3f" % values[0, 5])
    l6.set("6: " + "%.3f" % values[0, 6])
    l7.set("7: " + "%.3f" % values[0, 7])
    l8.set("8: " + "%.3f" % values[0, 8])
    l9.set("9: " + "%.3f" % values[0, 9])


global image1
global imgDupe
global root

global l0
global l1
global l2
global l3
global l4
global l5
global l6
global l7
global l8
global l9


width = height = 56
root = Tk()

#Label Variables
l0 = StringVar()
l0.set("0: ")
l1 = StringVar()
l1.set("1: ")
l2 = StringVar()
l2.set("2: ")
l3 = StringVar()
l3.set("3: ")
l4 = StringVar()
l4.set("4: ")
l5 = StringVar()
l5.set("5: ")
l6 = StringVar()
l6.set("6: ")
l7 = StringVar()
l7.set("7: ")
l8 = StringVar()
l8.set("8: ")
l9 = StringVar()
l9.set("9: ")

#Canvas Properties
canvas = Canvas(root, width=width, height=height, bg='white')
#canvas.pack(side=TOP)
canvas.grid(row = 0, column = 0, sticky = W, pady = 2)
canvas.old_coords = None

image1 = Image.new("RGB", (width, height), (255,255,255) )
imgDupe = ImageDraw.Draw(image1)

#Window Properties
topFrame = Frame(root)
botFrame = Frame(root)
root.resizable(False, False)
root.geometry("250x350")
root.title("AiProj")
root.bind('<B1-Motion>', draw)
root.bind('<Button-3>', clearCanvas)
root.bind('<Motion>', updateMouseLoc)

Button1 = Button(root, text='Get Picture', fg='Black', command=lambda: saveImage("Test.png", image1))
Button2 = Button(root, text='Test Image', fg='Black', command=lambda: testNumber())

label0 = Label(root, textvariable=l0)
label1 = Label(root, textvariable=l1)
label2 = Label(root, textvariable=l2)
label3 = Label(root, textvariable=l3)
label4 = Label(root, textvariable=l4)
label5 = Label(root, textvariable=l5)
label6 = Label(root, textvariable=l6)
label7 = Label(root, textvariable=l7)
label8 = Label(root, textvariable=l8)
label9 = Label(root, textvariable=l9)
drawDescr_Label = Label(root, text="Left click to draw on Canvas.")
eraseDescr_Label = Label(root, text="Right click to erase.")


AI.initAI()

#label9.pack(side=RIGHT)
#label8.pack(side=RIGHT)
#label7.pack(side=RIGHT)
#label6.pack(side=RIGHT)
#label5.pack(side=RIGHT)
#label4.pack(side=RIGHT)
#label3.pack(side=RIGHT)
#label2.pack(side=RIGHT)
#label1.pack(side=RIGHT)
#label0.pack(side=RIGHT)

label0.grid(row = 1, column = 8, sticky = W, pady = 2)
label1.grid(row = 2, column = 8, sticky = W, pady = 2)
label2.grid(row = 3, column = 8, sticky = W, pady = 2)
label3.grid(row = 4, column = 8, sticky = W, pady = 2)
label4.grid(row = 5, column = 8, sticky = W, pady = 2)
label5.grid(row = 6, column = 8, sticky = W, pady = 2)
label6.grid(row = 7, column = 8, sticky = W, pady = 2)
label7.grid(row = 8, column = 8, sticky = W, pady = 2)
label8.grid(row = 9, column = 8, sticky = W, pady = 2)
label9.grid(row = 10, column = 8, sticky = W, pady = 2)
drawDescr_Label.grid(row = 2, column = 0, sticky = W, pady = 2)
eraseDescr_Label.grid(row = 3, column = 0, sticky = W, pady = 2)
Button1.grid(row = 4, column = 0, sticky = W, pady = 2)
Button2.grid(row = 5, column = 0, sticky = W, pady = 2)
#Button1.Grid(side=LEFT)
#Button2.pack(side=LEFT)

root.mainloop()