import pygame as py
from tkinter import *
import Button
import WindowGrid
import ShapesInGrid
import ChangeColor
import initials
import Mathematics

#αρχικοποιώ τις Global variables
initials.init()

# Παίρνουμε τις τιμές της ανάλυσης του monitor για αυτό κανουμε import την tkinter
root = Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

py.init()
# δημιουργώ παράθυρο το οποίο είναι μεταβαλλόμενο
window = py.display.set_mode((width, height - 60), py.RESIZABLE)
title = 'Ειδική Θεωρία της Σχετικότητας - Οπτικοποίηση Φαινομένων'
py.display.set_caption(title)


# Φορτώνουμε τις εικόνες για τα κουμπιά του αρχικού Μενού
start_img1 = py.image.load('Button_1.jpg')
exit_img = py.image.load('Button_2.jpg')
rect_img = py.image.load('rect_1.png')
triangle_img = py.image.load('triangle_1.png')
change_Color_img = py.image.load('change_Color.png')
lysh_img=py.image.load('lysh.png')
systhma_kinoumeno_img=py.image.load('systhma_kinoumeno.png').convert()
systhma_paratiriti_img=py.image.load('systhma_paratiriti.png')
red_img1= py.image.load('red.png')
green_img1= py.image.load('green.png')
yellow_img1= py.image.load('yellow.png')
orange_img1= py.image.load('orange.png')
blue_img1= py.image.load('blue.png')
violet_img1= py.image.load('violet.png')
dexia_img1= py.image.load('dexia.png')
aristera_img1= py.image.load('aristera.png')
pososto10_img1 =py.image.load('10_ta_100.png')
pososto20_img1 =py.image.load('20_ta_100.png')
pososto30_img1 =py.image.load('30_ta_100.png')
pososto40_img1 =py.image.load('40_ta_100.png')
pososto50_img1 =py.image.load('50_ta_100.png')
pososto60_img1 =py.image.load('60_ta_100.png')
pososto70_img1 =py.image.load('70_ta_100.png')
pososto80_img1 =py.image.load('80_ta_100.png')
pososto90_img1 =py.image.load('90_ta_100.png')
pososto100_img1 =py.image.load('100_ta_100.png')



#Μεταβλητές που αφορουν στην λειτουργία του παιχνιδιού
menu_state = 'main' #κατάσταση αρχικού μενού
game_paused = True



#φτιάχνουμε τα αρχικά κουμπιά
start_button = Button.Button(width/4, height/3, start_img1, 1)
exit_button = Button.Button(width/2, height/3, exit_img, 1)
rect_button = Button.Button(width/2.5, height/5, rect_img, 1)
triangle_button = Button.Button(width/2.5, height/2, triangle_img, 1)
red_button= Button.Button(width/2, height/6, red_img1, 1)
orange_button= Button.Button(width/4, height/6, orange_img1, 1)
green_button= Button.Button(width/2, height/3, green_img1, 1)
blue_button= Button.Button(width/4, height/3, blue_img1, 1)
violet_button= Button.Button(width/4, height/2, violet_img1, 1)
yellow_button= Button.Button(width/2, height/2, yellow_img1, 1)

dexia_button = Button.Button(width/2.5, height/5, dexia_img1, 1)
aristera_button = Button.Button(width/2.5, height/2, aristera_img1, 1)

pososto10_button= Button.Button(100, 0, pososto10_img1, 1)
pososto20_button= Button.Button(500, 0, pososto20_img1, 1)
pososto30_button= Button.Button(900, 0, pososto30_img1, 1)
pososto40_button= Button.Button(100, 200, pososto40_img1, 1)
pososto50_button= Button.Button(500, 200, pososto50_img1, 1)
pososto60_button= Button.Button(900, 200, pososto60_img1, 1)
pososto70_button= Button.Button(100, 400, pososto70_img1, 1)
pososto80_button= Button.Button(500, 400, pososto80_img1, 1)
pososto90_button= Button.Button(900, 400, pososto90_img1, 1)
pososto100_button= Button.Button(width/3, 600, pososto100_img1, 1)


change_Color_button = Button.Button(width/2.5, height/20, change_Color_img, 1)
lysh_button = Button.Button(width/2.5, height/3, lysh_img, 1)

play = True
while play:
    window.fill('purple')

    #κάνει παύση το παιχνίδι
    if game_paused == True:
        #Δημιουργία μενού
        #αρχικό μενου
        if menu_state == 'main':
            #κουμπιά μενού
            if start_button.draw(window):
                menu_state = 'fainomena'
            if exit_button.draw(window):
                exit()
        if menu_state == 'fainomena':
            #κουμπιά μενού
            if change_Color_button.draw(window):
                menu_state = 'kateythynsi_taxythtas'
        if menu_state == 'kateythynsi_taxythtas':
            if dexia_button.draw(window):
                initials.polaplasiasths =1
                menu_state = 'pososto_c'
            if aristera_button.draw(window):
                initials.polaplasiasths =-1
                menu_state = 'pososto_c'
        if menu_state == 'pososto_c':
            if pososto10_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.1
                menu_state='xrwmata'
                print(initials.x_velocity)
            if pososto20_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.2
                menu_state='xrwmata'
            if pososto30_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.3
                menu_state='xrwmata'
            if pososto40_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.4
                menu_state='xrwmata'
            if pososto50_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.5
                menu_state='xrwmata'
            if pososto60_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.6
                menu_state='xrwmata'
            if pososto70_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.7
                menu_state='xrwmata'
            if pososto80_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.8
                menu_state='xrwmata'
            if pososto90_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*0.9
                menu_state='xrwmata'
            if pososto100_button.draw(window):
                initials.x_velocity=initials.polaplasiasths*1
                menu_state='xrwmata'
        if menu_state =='xrwmata':
            if red_button.draw(window):
                initials.idiocolor='red'
                initials.idiofreq = 451*pow(10,12)
                menu_state='sxhmata'
            if yellow_button.draw(window):
                initials.idiocolor='yellow'
                initials.idiofreq = 521 *pow(10,12)
                menu_state = 'sxhmata'
            if orange_button.draw(window):
                initials.idiocolor='orange'
                initials.idiofreq = 493 *pow(10,12)
                menu_state = 'sxhmata'
            if green_button.draw(window):
                initials.idiocolor='green'
                initials.idiofreq = 565 *pow(10,12)
                menu_state = 'sxhmata'
            if blue_button.draw(window):
                initials.idiocolor='blue'
                initials.idiofreq = 640 * pow(10,12)
                menu_state = 'sxhmata'
            if violet_button.draw(window):
                initials.idiocolor='violet'
                initials.idiofreq = 715 *pow(10,12)
                menu_state = 'sxhmata'
        #Επόμενο υπομενού
        if menu_state == 'sxhmata':
            #κουμπιά υπομενού
            if rect_button.draw(window):
                menu_state = 'tetragwno'
            if triangle_button.draw(window):
                menu_state = 'trigwno'
        #Τετράγωνο
        if menu_state == 'tetragwno':
            window.fill('white')
            WindowGrid.grid(window, width, height)
            #θα μηδενίσουμε τις coords σε περιπτωση που ειχαμε τρεξει πριν να σβησει τις προηγουμενες
            initials.xcoords=[]
            initials.ycoords=[]
            ShapesInGrid.rect_in_grid(window,10,0)
            window.blit(systhma_kinoumeno_img,(40,440))

            if lysh_button.draw(window):
                menu_state='lysh_1'
        if menu_state =='lysh_1':

            WindowGrid.grid(window, width, height)
            #(xcoords,ycoords) =
            ShapesInGrid.rect_in_grid(window,10,0)
            window.blit(systhma_kinoumeno_img, (40, 440))
            Mathematics.photon_frequency_in_obs_system()
            Mathematics.color_in_obsosystem()
            initials.xcoords_paratiriti=[]
            initials.ycoords_paratiriti = []
            ChangeColor.Change_rect_Color_in_grid(window, 10,600)
            window.blit(systhma_paratiriti_img, (640, 440))

        #Τρίγωνο
        if menu_state == 'trigwno':
            window.fill('white')
            WindowGrid.grid(window, width, height)
            #(xcoords,ycoords) =
            initials.xcoords=[]
            initials.ycoords=[]
            ShapesInGrid.triangle_in_grid(window,10,0)
            window.blit(systhma_kinoumeno_img, (40, 440))

            if lysh_button.draw(window):
                menu_state = 'lysh_2'
        if menu_state == 'lysh_2':
            window.fill('white')
            WindowGrid.grid(window, width, height)
            # (xcoords,ycoords) =
            ShapesInGrid.triangle_in_grid(window, 10, 0)
            window.blit(systhma_kinoumeno_img, (40, 440))
            Mathematics.photon_frequency_in_obs_system()
            Mathematics.color_in_obsosystem()
            initials.xcoords_paratiriti=[]
            initials.ycoords_paratiriti = []
            ChangeColor.Change_triangle_Color_in_grid(window, 10, 600)
            window.blit(systhma_paratiriti_img, (640, 440))



        for event in py.event.get():
            #ελεγχει εάν πατησει ένα κουμπί και εαν αυτο είναι το space μας πηγαίνει στο αρχικό μενού
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    game_paused = True
                    menu_state = 'main'
            if event.type == py.QUIT:
                exit()

            py.display.update()
