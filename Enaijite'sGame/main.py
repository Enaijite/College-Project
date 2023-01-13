import random
import pygame
import sys
import pygame as pg
import os
from pygame.locals import *
from settings import*
from sprites import*
from Buttons import*
from UI import*
from level import*

class Game:
    def __init__(self):
        #initialize game window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((width,height))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        #puts the platforms onto the screen
        self.level = Level(level_map,self.screen)
        #font
        self.font_name = pg.font.match_font(font_name)
        #game attributes
        self.max_health = 100
        self.cur_health = 100
        #running
        self.running = True
        #UI
        self.ui = UI(self.screen)

    def run(self):
        #Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.level.all_sprites.update()
            self.draw()

        
    def events(self):
        #Game Loop - events
        pg.init()
        keys = pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                    self.running = False

    def enemy_attack(self):
        hits = pg.sprite.spritecollide(self, self.game.player, False)
        if hits and self.image == pygame.image.load(os.path.join(img_folder, "sprite_Attack.png")):
            self.cur_health -= 10

##    def timer(self):
##        total_seconds = frame_count // FPS
##        minutes =  total_seconds // 60
##        seconds = total_seconds % 60
##        output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
##        text = self.draw_text(output_string, 40, WHITE, 1200,20)
##        on = False
##        while not on:
##            seconds += 1
##            if seconds == 60:4
##                seconds = 0
##                minuites += 1
##        
                
                       
    def draw(self):
        #Game Loop - draw
        self.level.run()
        #self.all_sprites.draw(self.screen)
        self.ui.show_health(self.cur_health,self.max_health)
        #self.timer()
        #flip the screen
        pg.display.flip()


    def show_start_screen(self):
        self.screen = pg.display.set_mode((width,height))
        self.screen.fill(BLACK)
        b1 = button(self.screen, (305, 200), "Quit")
        b2 = button(self.screen, (300, 100), "Start")
        b3 = button(self.screen, (295, 300), "Options")
        pg.display.flip()
        pg.init()
        IDK = True
        while IDK:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    IDK = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        IDK = False
                        pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b1.collidepoint(pygame.mouse.get_pos()):
                        IDK = False
                        pygame.quit()
                    if b2.collidepoint(pygame.mouse.get_pos()):
                        IDK = False
                    if b3.collidepoint(pygame.mouse.get_pos()):
                        self.Controls_Screen()
        pg.display.init()

    def Controls_Screen(self):
        A = True
        while A:
            self.screen = pg.display.set_mode((width,height))
            self.screen.fill(BLACK)
            self.draw_text("Use arrow keys to move", 20, WHITE, 100, 50)
            self.draw_text("You can also use WASD to move", 20, WHITE, 120, 100)
            b5 = button(self.screen, (50, 200), "BacK")
            pg.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    A = False
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b5.collidepoint(pygame.mouse.get_pos()):
                        self.show_start_screen()
                        A = False

    
    def show_go_screen(self):
        #game over screen
        pass

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
   
g = Game()
g.show_start_screen()
while g.running:
    g.run()
    g.show_go_screen()

pg.quit()
