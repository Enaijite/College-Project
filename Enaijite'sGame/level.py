import pygame
from sprites import*
from settings import*

vec = pg.math.Vector2

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.screen = pg.display.set_mode((width,height))
        
    def setup_level(self,level_data):
        self.platforms = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy_sprites = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        for row_index,row in enumerate(level_data):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    platform = Platform((x,y),tile_size)
                    self.platforms.add(platform)
                if cell == "P":
                    player_sprite = Player(self,(x),(y))
                    self.player.add(player_sprite)
                if cell == "E":
                    enemy = Enemy(self,(x),(y))
                    self.enemy_sprites.add(enemy)
   
        
    def run(self):
        self.screen.fill(SKY)
        #levelplatforms
        self.platforms.draw(self.display_surface)
        #draw player
        self.player.draw(self.display_surface)
        #draw enemy
        self.enemy_sprites.draw(self.display_surface)
        self.player.update()
        self.enemy_sprites.update()
        
        

        
        



        
