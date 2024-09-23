import pygame as py


###Εδώ θα κάνουμε την αρχικοποίηση όλων των global μεταβλητών μας
def init():
    #Συντεταγμένες σχήματος στο ιδιοσύστημα του
    global xcoords
    global ycoords
    #συντεταγμένες στο συστημα παρατηρητή
    global xcoords_paratiriti
    global ycoords_paratiriti
    #χρώμα στο σύστημα ιδιοσύστημα του σχήματος
    global color
    #χρώμα στο σύστημα παρατηρητή
    xcoords=[]
    ycoords=[]
    xcoords_paratiriti=[]
    ycoords_paratiriti=[]



    #Συχνότητα στο ιδιοσύστημα του σώματος
    global idiofreq
    idiofreq = 0
    global idiocolor
    idiocolor=''
    # Συχνότητα στο σύστημα του ακίνητου παρατηρητη
    global obsfreq
    obsfreq=0
    global obscolor
    obscolor=''

    global x_velocity#ταχύτητα στον άξονα χ
    global polaplasiasths
    polaplasiasths = 1
    x_velocity =0.5
    global y_velocity    #ταχύτητα στον άξονα y
    global gamma          #συντελεστής γ

