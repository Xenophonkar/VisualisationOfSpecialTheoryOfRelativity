import pygame as py
from tkinter import *

def grid(surface, width, height):
    distanceBtwRows= 20
    rows=height/distanceBtwRows
    Collums = width / distanceBtwRows
    x=0
    y=0
    #κάθετες γραμμές
    for l in range(int(Collums)):
        x+=distanceBtwRows
        py.draw.line(surface, 'black', (x, 0), (x, height))
    #οριζόντιες γραμμές
    for l in range(int(rows)):
        y+=distanceBtwRows
        py.draw.line(surface, 'black', (0, y), (width, y))