#sprite classes for platform game
import pygame as pg
from settings import*
import os
import pygame, sys
from pygame.locals import*

vec = pg.math.Vector2

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,"img")

class Player(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        self.game = game
        pg.sprite.Sprite.__init__(self)
        self.screen = pg.display.set_mode((width,height))
        self.image = pg.Surface((30,40))
        self.image = self.image = pygame.image.load(os.path.join(img_folder, "sprite.png")).convert()
        self.image.set_colorkey(GREEN)
        self.pos = vec(x,y)
        self.rect = self.image.get_rect()

        #movement
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        #sprite goes into and out of the platform, if the sprite collides with the platform they will be sent up
        #makes sprite only able to jump if on a platform
        self.rect.y += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -15

    def update(self):
        self.acc = vec(0, PLAYER_GRAV)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]or keys[pg.K_d]:
            self.acc.x = PLAYER_ACC
        if keys[pg.K_SPACE] or keys[pg.K_w]:
            self.jump()
        if keys[pg.K_z]:
            self.Attack()

        #after sprite attack the sprite reverts back to it's original sprite
        #so the attack only lasts a few seconds
        for event in pg.event.get():
            if event.type == pygame.USEREVENT:
                self.image = pygame.image.load(os.path.join(img_folder, "sprite.png")).convert()
                self.image.set_colorkey(GREEN)
            
           
        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        #if wrap around the screen
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width

        self.rect.x = self.pos.x
        self.collide_horizontally()
        self.rect.y = self.pos.y
        self.collide_vertically()
        
    def collide_horizontally(self):
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        collision = []
        for hit in hits:
            collision.append(hit.rect)
        try:
            lowest_hit = min(collision) #min(collision gives an error when len=0)

            #if the velocity is negative then character is moving left
            if self.vel.x < 0:
                self.rect.left = lowest_hit.right
                # recursion here is used to reduce players clipping through walls
                # This solution requires all walls to be thicker
                
                # The more walls in a row the map has, the faster the player will move without clipping
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if len(hits) > 0:
                    self.rect.x += 1
                    self.collide_horizontally()
                    self.rect.x -=1
                self.vel.x = 0
                # if the velocity is positive then character is moving right
            elif self.vel.x > 0:
                self.rect.right = lowest_hit.left
                # recursion is repeated in the other side
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if len(hits) > 0:
                    self.rect.x -= 1
                    self.collide_horizontally()
                    self.rect.x+=1
                self.vel.x = 0
        except:
            pass
        self.pos.x = self.rect.x

    def collide_vertically(self):
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        collision = []
        for hit in hits:
            collision.append(hit.rect)
        try:
            lowest_hit = max(collision)
            if self.vel.y > 0:
                self.rect.bottom = lowest_hit.top
                self.air_timer = 0
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if len(hits) > 0:
                    self.rect.y -= 1
                    self.collide_vertically()
                self.vel.y = 0
            elif self.vel.y < 0:
                self.rect.top = lowest_hit.bottom
                self.jump_cut()
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if len(hits) > 0:
                    self.rect.y += 1
                    self.collide_vertically()
                self.vel.y = 0
        except:
            pass
        self.pos.y = self.rect.y

    def Attack(self):
        #chcanges player sprite image when the player presses z then reverts back to original after some time elapsed
        self.image = pygame.image.load(os.path.join(img_folder, "sprite_Attack.png")).convert()
        self.image.set_colorkey(GREEN)
        hits = pg.sprite.spritecollide(self, self.game.enemy_sprites, True)
        if hits and self.image == pygame.image.load(os.path.join(img_folder, "sprite_Attack.png")):
            print("enemy dead")   
        pygame.time.set_timer(pygame.USEREVENT, 100)
            

            
class Platform(pg.sprite.Sprite):
    def __init__(self,pos,size):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((size,size))
        self.image.fill(BLUE)
        #self.image = pygame.image.load(os.path.join(img_folder, "Grass.png")).convert()
        self.rect = self.image.get_rect(topleft = pos)
        

class Enemy(pg.sprite.Sprite):
    def __init__(self,game,x,y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((20,30))
        self.image = pygame.image.load(os.path.join(img_folder, "Tank Demon.png")).convert()
        self.image.set_colorkey(GREEN)
        self.rect = self.image.get_rect()
        self.pos = vec(x,y)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def update(self):
        self.acc = vec(0, ENEMY_GRAV)
     
        #apply friction
        self.acc.x += self.vel.x * ENEMY_FRICTION
        #equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #if wrap around the screen
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width

        self.rect.x = self.pos.x
        self.collide_horizontally()
        self.rect.y = self.pos.y
        self.collide_vertically()

    def collide_horizontally(self):
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        collision = []
        for hit in hits:
            collision.append(hit.rect)
        try:
            lowest_hit = min(collision) #min(collision gives an error when len=0)

            #if the velocity is negative then character is moving left
            if self.vel.x < 0:
                self.rect.left = lowest_hit.right
                # recursion here is used to reduce players clipping through walls
                # This solution requires all walls to be thicker
                
                # The more walls in a row the map has, the faster the player will move without clipping
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if len(hits) > 0:
                    self.rect.x += 1
                    self.collide_horizontally()
                    self.rect.x -=1
                self.vel.x = 0
                # if the velocity is positive then character is moving right
            elif self.vel.x > 0:
                self.rect.right = lowest_hit.left
                # recursion is repeated in the other side
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if len(hits) > 0:
                    self.rect.x -= 1
                    self.collide_horizontally()
                    self.rect.x+=1
                self.vel.x = 0
        except:
            pass
        self.pos.x = self.rect.x

    def collide_vertically(self):
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        collision = []
        for hit in hits:
            collision.append(hit.rect)
        try:
            lowest_hit = max(collision)
            if self.vel.y > 0:
                self.rect.bottom = lowest_hit.top
                self.air_timer = 0
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if len(hits) > 0:
                    self.rect.y -= 1
                    self.collide_vertically()
                self.vel.y = 0
            elif self.vel.y < 0:
                self.rect.top = lowest_hit.bottom
                self.jump_cut()
                hits = pg.sprite.spritecollide(self, self.game.platforms, False)
                if len(hits) > 0:
                    self.rect.y += 1
                    self.collide_vertically()
                self.vel.y = 0
        except:
            pass
        self.pos.y = self.rect.y



        

            
