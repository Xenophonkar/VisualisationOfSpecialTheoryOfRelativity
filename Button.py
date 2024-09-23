import pygame as py

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = py.transform.scale(image,(int(width*scale),int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft =(x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        pos =py.mouse.get_pos()

        #Ελέγχω εαν το ποντικι είναι πάνω απο την εικόνα
        if self.rect.collidepoint(pos):
            #ελέγχω εαν έκανα click στο κουμπί
            if py.mouse.get_pressed()[0] ==1 and self.clicked ==False:
                self.clicked = True
                action = True

            if py.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #Σχεδιάζω το κουμπί στην οθόνη
        surface.blit(self.image,(self.rect.x,self.rect.y))

        #Η συναρτηση draw επιστρέφει την μεταβλητή action που την χρησιμοποιώ στο πρόγραμμα
        return action