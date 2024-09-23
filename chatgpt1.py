import pygame
import sys


class Button:
    def __init__(self, x, y, width, height, inactive_color, active_color, text, font_size=30):
        self.rect = pygame.Rect(x, y, width, height)
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.clicked = False

    def is_mouse_over(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface):
        action = False
        pygame.draw.rect(surface, self.inactive_color, self.rect)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            # ελέγχω εαν έκανα click στο κουμπί
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                self.inactive_color, self.active_color = self.active_color, self.inactive_color
            else:
                self.inactive_color, self.active_color = self.active_color, self.inactive_color

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False





    def update(self):
        if self.is_mouse_over():
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                # ελέγχω εαν έκανα click στο κουμπί
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    action = True
                    self.inactive_color, self.active_color = self.active_color, self.inactive_color
                else:
                    self.inactive_color, self.active_color = self.active_color, self.inactive_color

                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False




# Initialize Pygame
pygame.init()

# Create a Pygame display surface
surface = pygame.display.set_mode((640, 480))

# Create the main menu buttons
resume_button = Button(200, 100, 200, 50, (255, 0, 0), (0, 255, 0), "Resume")
options_button = Button(200, 200, 200, 50, (255, 0, 0), (0, 255, 0), "Options")
exit_button = Button(200, 300, 200, 50, (255, 0, 0), (0, 255, 0), "Exit")

# Create the options menu buttons
music_button = Button(200, 100, 200, 50, (255, 0, 0), (0, 255, 0), "Music")
graphics_button = Button(200, 200, 200, 50, (255, 0, 0), (0, 255, 0), "Graphics")
back_button = Button(200, 300, 200, 50, (255, 0, 0), (0, 255, 0), "Back")

# Create a separate surface for each menu
main_menu_surface = pygame.Surface((640, 480))
options_menu_surface = pygame.Surface((640, 480))

# Set up the main menu and options menu
main_menu_buttons = [resume_button, options_button, exit_button]
options_menu_buttons = [music_button, graphics_button, back_button]

# Set the default active menu to be the main menu
active_menu_buttons = main_menu_buttons
active_menu_surface = main_menu_surface


def draw_buttons(buttons, surface):
    for button in buttons:
        button.draw(surface)


def update_buttons(buttons):
    for button in buttons:
        button.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for button in active_menu_buttons:
                if button.is_mouse_over():
                    if button == resume_button:
                        # Resume the game
                        pass
                    elif button == options_button:
                        # Switch to the options menu
                        active_menu_buttons = options_menu_buttons
                        active_menu_surface = options_menu_surface
                    elif button == exit_button:
                        # Exit the game
                        pygame.quit()
                        sys.exit()

                    ##the_options_menu_buttons
                    elif button == back_button:
                        active_menu_buttons = main_menu_buttons
                        active_menu_surface = main_menu_surface

                    # Update and redraw the buttons
    update_buttons(active_menu_buttons)
    active_menu_surface.fill((0, 0, 0))
    draw_buttons(active_menu_buttons, active_menu_surface)

    # Draw the active menu surface to the display surface
    surface.blit(active_menu_surface, (0, 0))

    # Update the display
    pygame.display.flip()
