import pygame as py
import initials

def rect_in_grid(surface,x1,x):
    global width, height
    distanceBtwRows = 40
    y = 0
    for i in range(x1):
        initials.xcoords.append(x + distanceBtwRows)
        x += distanceBtwRows
        initials.ycoords.append(y + distanceBtwRows)
        y += distanceBtwRows
    for k in range(x1):
        for j in range (x1):
            py.draw.circle(surface,initials.idiocolor,(initials.xcoords[k],initials.ycoords[j]),5)
    #Επιστρέφει την τιμη των πινάκων των συντεταγμένων
    #return xcoords, ycoords

def triangle_in_grid(surface,x1,x):
    distanceBtwRows = 40
    x2=x1
    while x2>0:
        y = distanceBtwRows * (x2)
        for i in range (x2):
            initials.xcoords.append(x+distanceBtwRows)
            x += distanceBtwRows
            initials.ycoords.append(y)
        for k in range(len(initials.xcoords)):
            py.draw.circle(surface, initials.idiocolor, (initials.xcoords[k],initials.ycoords[k]), 5)
        x=(x- (x2*distanceBtwRows)+distanceBtwRows/2)
        x2 = x2 - 1
    # Επιστρέφει την τιμη των πινάκων των συντεταγμένων
    #return xcoords, ycoords

