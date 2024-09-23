import pygame as py
import initials

def Change_rect_Color_in_grid(surface,x1,x):
    global width, height
    distanceBtwRows = 40
    x = 600
    y = 0
    for i in range(x1):
        initials.xcoords_paratiriti.append(x + distanceBtwRows)
        x += distanceBtwRows
        initials.ycoords_paratiriti.append(y + distanceBtwRows)
        y += distanceBtwRows
    for k in range(x1):
        for j in range(x1):
            py.draw.circle(surface, initials.obscolor, (initials.xcoords_paratiriti[k], initials.ycoords_paratiriti[j]), 5)

def Change_triangle_Color_in_grid(surface,x1,x):
    distanceBtwRows = 40
    x2=x1
    while x2>0:
        y = distanceBtwRows * (x2)
        for i in range (x2):
            initials.xcoords_paratiriti.append(x+distanceBtwRows)
            x += distanceBtwRows
            initials.ycoords_paratiriti.append(y)
        for k in range(len(initials.xcoords_paratiriti)):
            py.draw.circle(surface, initials.obscolor, (initials.xcoords_paratiriti[k],initials.ycoords_paratiriti[k]), 5)
        x=(x- (x2*distanceBtwRows)+distanceBtwRows/2)
        x2 = x2 - 1