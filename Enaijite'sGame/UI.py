import pygame
import os
from pygame.locals import*
from settings import*

#images file path
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

class UI:
    def __init__(self,surface):

        #setup
        self.display_surface = surface

        #health
        self.health_bar = pygame.image.load(os.path.join(img_folder, "healthbar.png"))
        self.health_bar_topleft = (90,18)
        self.bar_max_width = 106
        self.bar_height = 22

    def show_health(self, current, full):
        #make health bar show on screen
        self.display_surface.blit(self.health_bar,(45,15))
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,RED,health_bar_rect)


