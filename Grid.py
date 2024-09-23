import pygame as py
from tkinter import *
import Button


def grid(window, width, height):
    distanceBtwRows= 20
    rows=height/distanceBtwRows
    Collums = width / distanceBtwRows
    x=0
    y=0
    #κάθετες γραμμές
    for l in range(int(Collums)):
        x+=distanceBtwRows
        py.draw.line(window, 'black', (x, 0), (x, height))
    for l in range(int(rows)):
        y+=distanceBtwRows
        py.draw.line(window, 'black', (0, y), (width, y))

#Δημιουργούμε ενα τετράγωνο στο πλέγμα με x1 x x1 σημεία και κρατάμε τις συντεταγμένες των σημείων
def rect_in_grid(window,x1):
    global xcoords, ycoords
    distanceBtwRows = 20
    xcoords =[]
    ycoords =[]
    x = 0
    y = 0
    for i in range(x1):
        xcoords.append(x + distanceBtwRows)
        x += distanceBtwRows
        ycoords.append(y + distanceBtwRows)
        y += distanceBtwRows
    for k in range(x1):
        for j in range (x1):
            py.draw.circle(window,'red',(xcoords[k],ycoords[j]),5)


def triangle_in_grid(window,x1):
    global xcoords, ycoords
    distanceBtwRows = 20
    xcoords =[]
    ycoords =[]
    x = 0
    x2=x1
    while x2>0:
        y = distanceBtwRows * (x2)
        for i in range (x2):
            xcoords.append(x+distanceBtwRows)
            x += distanceBtwRows
            ycoords.append(y)
        for k in range(len(xcoords)):
            py.draw.circle(window, 'red', (xcoords[k], ycoords[k]), 5)
        x=(x- (x2*distanceBtwRows)+distanceBtwRows/2)
        x2 = x2 - 1


    print(xcoords)
    print(ycoords)
    print(x2)

  #  for k in range(x1):
  #      pygame.draw.circle(window, 'red', ((x + distanceBtwRows), (y + distanceBtwRows)), 5)
  #      x += distanceBtwRows
  #  for l in range(x1):
  #      pygame.draw.circle(window, 'red', (x, (y + distanceBtwRows)), 5)
  #      y += distanceBtwRows
  #  for k in range(x1-1):
  #      pygame.draw.circle(window, 'red', ((x - distanceBtwRows), y), 5)
   #     x -= distanceBtwRows
  #  for k in range(x1-1):
  #      pygame.draw.circle(window, 'red', (x, (y - distanceBtwRows)), 5)
   #     y -= distanceBtwRows

def redraw(window):
    global width,height
    window.fill('white')

    grid(window, width, height)
    #rect_in_grid(window,4)
    triangle_in_grid(window,4)
    py.display.update()

def main():
    global width,height
    global xcoords
    global ycoords

    #Παίρνουμε τις τιμές της ανάλυσης του monitor για αυτό κανουμε import την tkinter
    root = Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()


    py.init()
    #δημιουργώ παράθυρο το οποίο είναι μεταβαλλόμενο
    window=py.display.set_mode((width,height-60),py.RESIZABLE)
    title= 'Ειδική Θεωρία της Σχετικότητας - Οπτικοποίηση Φαινομένων'
    py.display.set_caption(title)

    # Φορτώνουμε τις εικόνες για τα κουμπιά του αρχικού Μενού
    start_img1 = py.image.load('Button_1.jpg')
    exit_img = py.image.load('Button_2.jpg')

    start_button = Button.Button(50,200,start_img1,1)
    exit_button = Button.Button(100,200,exit_img,1)
    play=True
    while play:

        start_button.draw(window)
        exit_button.draw(window)

        if start_button.draw(window):
            print('START')
        if exit_button.draw(window):
            print('EXIT')

        for event in py.event.get():
            if event.type==py.QUIT:
                exit()

        redraw(window)



main()
