import random 
from konstanter import *
import pygame as pg

surface = pg.display.set_mode(SIZE)

game_over = 0
main_menu = True
 
type_picture = 0
dead_picture = 0
checkpoint = pg.image.load('Bilder/10.png')
checkpoint = pg.transform.scale(checkpoint, (tile_size, tile_size * 2))

restart_img = pg.image.load('Bilder/restart.png')
start_img = pg.image.load('Bilder/start.png')
exit_img = pg.image.load('Bilder/exit.png')



background_img1 = pg.image.load('Bilder/background_img1.png')
background_img2 = pg.image.load('Bilder/background_img2.png')
background_img4 = pg.image.load('Bilder/background_img4.png')

def Background_img(image): 
    size = pg.transform.scale(image,(WIDTH, HEIGHT))
    surface.blit(size, (0,0))



images = []

class World(): 
    def __init__(self, data):
        self.tile_list = []
        for i in range(1,11):
            dirt_img = pg.image.load(f'Bilder/{i}.png')
            images.append(dirt_img)
        row_count = 0

        for row in data: 
            column_count = 0

            for tile in row: 
                if tile == 1: 
                    img = pg.transform.scale(images[0], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pg.transform.scale(images[1], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3: 
                    img = pg.transform.scale(images[2], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size 
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4: 
                    img = pg.transform.scale(images[3], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size 
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5: 
                    img = pg.transform.scale(images[4], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size 
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6: 
                    img = pg.transform.scale(images[5], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size 
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7: 
                    img = pg.transform.scale(images[6], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size 
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 8: 
                    img = pg.transform.scale(images[7], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size 
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 9: 
                    img = pg.transform.scale(images[9], (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = column_count * tile_size 
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 11: 
                    enemy = Enemy(column_count * tile_size, row_count * tile_size + 7)
                    enemy_group1.add(enemy)
                if tile == 12: 
                    enemy = Enemy(column_count * tile_size, row_count * tile_size + 7)
                    enemy_group2.add(enemy)
                if tile == 13: 
                    lava = Lava(column_count * tile_size, row_count * tile_size + tile_size // 2)
                    lava_group1.add(lava)
                if tile == 14: 
                    lava = Lava(column_count * tile_size, row_count * tile_size + tile_size // 2)
                    lava_group2.add(lava)
                column_count += 1
            row_count += 1 

    def draw(self):
        for tile in self.tile_list: 
            surface.blit(tile[0], tile[1])
        surface.blit(checkpoint, (tile_size * 15, tile_size * 2))

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self):
        action = False
        pos = pg.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                action = True
                self.clicked = True
        
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
                


        surface.blit(self.image, self.rect)

        return action
    
class Flag(): 
    def __init__(self, x, y): 
        self.x = x
        self.y = y
        self.rect = pg.Rect(x, y, tile_size, tile_size * 2)


def level_complete():
    global game_over 
    if player1.rect.colliderect(flag1.rect) and player2.rect.colliderect(flag1.rect):
        return True
    return False


class Player(): 
    def __init__(self, x, y, type_picture, dead_picture): 
        self.reset(x, y, type_picture, dead_picture)
        
    """ def jump(self): 
        if self.on_ground:
            self.vy = -15 """
            
    def draw(self):
        surface.blit(self.image, self.rect)
        

    def update(self, world, game_over):
        if game_over == 0:

            dx = self.vx
            dy = self.vy

            self.rect.y += self.vy
            self.rect.x += self.vx

            # Sjekker om spilleren er på bakken
            """ if self.y >= HEIGHT - self.size - tile_size: 
                self.y = HEIGHT - self.size - tile_size
                self.vy = 0
                self.on_ground = True 
                for tile in world.tile_list:
                    if self.x <= tile[1].x: 
                        self.x = tile[1].x 
                        self.vx = 0
                    elif self.x > tile[1].x + tile_size:
                        self.x = tile[1].x + tile_size 
                        self.vx = 0 """ 
                
                    
        
            # Tyngdekraft
            self.vy += 1
        
            if self.vy > 10: 
                self.vy = 10
            dy += self.vy

            # Kollisjon mellom spiller og map
            for tile in world.tile_list: 
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
            # Adjust player's horizontal position to stop movement
                    if dx > 0:
                        self.rect.right = tile[1].left - 4.9
                    elif dx < 0:
                        self.rect.left = tile[1].right + 4.9
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height): 
                        # Hoppe i en tile
                    if self.vy < 0: 
                        #dy = tile[1].bottom - self.rect.top
                        dy = 0
                        self.vy = 0

                        # Falle på en tile
                    elif self.vy >= 0: 
                        dy = tile[1].top - self.rect.bottom
                        self.vy = 0
                        self.on_ground = True
            
            # Sjekker kollisjon med enemies
            if pg.sprite.spritecollide(self, enemy_group1, False) and level != 2: 
                game_over = -1
            if pg.sprite.spritecollide(self, enemy_group2, False) and level != 1: 
                game_over = -1
                

            # Sjekker kollisjon med lava
            if pg.sprite.spritecollide(self, lava_group1, False) and level != 1: 
                game_over = -1
            if pg.sprite.spritecollide(self, lava_group2, False) and level != 2: 
                game_over = -1
                
                

            self.rect.x += dx
            self.rect.y += dy

            """ if self.rect.bottom < HEIGHT: 
                self.rect.bottom = HEIGHT
                dy = 0 """
            
        elif game_over == -1: 
            self.image = pg.transform.scale(pg.image.load('Bilder/ghost.png'), (tile_size, tile_size))
            self.rect.y -= 5
            
        return game_over

    def reset(self, x, y, type_picture, dead_picture):
        self.type_picture = type_picture
        self.dead_picture = dead_picture
    
        if type_picture == 0:
            img = pg.image.load(f'Bilder/player1.png')
        if type_picture == 1: 
            img = pg.image.load(f'Bilder/player2.png')
        self.image = pg.transform.scale(img, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vx = 0
        self.vy = 0
        self.on_ground = False # Hopping
        self.vertical_hit = False
        self.horizontal_hit = False
        

class Player1(Player):
    def __init__(self, x, y, type_picture, dead_picture):
        super().__init__(x, y, type_picture, dead_picture)
        self.direction = 1  # 1 for right, -1 for left

        player1_x = self.rect.x
        player1_y = self.rect.y

    def move(self):
        # Nullstiller farten
        self.vx = 0
        
        # Henter knappene fra tastaturet som trykkes på
        keys = pg.key.get_pressed()
        
        # Sjekker om tasten "d" er trykket på
        if keys[pg.K_d]:
            self.vx = PLAYER_VEL
            self.direction = 1  # Set direction to right
            
        # Sjekker om tasten "a" er trykket på
        if keys[pg.K_a]:
            self.vx = -PLAYER_VEL
            self.direction = -1  # Set direction to left

        if keys[pg.K_w] and self.on_ground == True: 
            self.vy = -8
            self.on_ground = False 

    def draw(self):
        # Flip image horizontally if direction is left
        if self.direction == -1:
            surface.blit(pg.transform.flip(self.image, True, False), self.rect)
        else:
            surface.blit(self.image, self.rect)

class Player2(Player):

    def __init__(self, x, y, type_picture, dead_picture):
        super().__init__(x, y, type_picture, dead_picture)
        self.direction = 1

        player2_x = self.rect.x
        player2_y = self.rect.y

    def move(self): 
        super().__init__
        # Nullstiller farten
        self.vx = 0
        
        # Henter knappene fra tastaturet som trykkes på
        keys = pg.key.get_pressed()
        
        # Sjekker om tasten "w" er trykket på
        if keys[pg.K_RIGHT]:
            self.vx = PLAYER_VEL
            self.direction = 1
            
        # Sjekker om tasten "s" er trykket på
        if keys[pg.K_LEFT]:
            self.vx = -PLAYER_VEL
            self.direction = -1

        if keys[pg.K_UP] and self.on_ground == True: 
            self.vy = -8
            self.on_ground = False
    def draw(self):
        # Flip image horizontally if direction is left
        if self.direction == -1:
            surface.blit(pg.transform.flip(self.image, True, False), self.rect)
        else:
            surface.blit(self.image, self.rect)

class Enemy(pg.sprite.Sprite): 
    def __init__(self, x, y): 
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('Bilder/enemy.png'), (tile_size / 1.2, tile_size / 1.2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if self.move_counter > 100: 
            self.move_direction *= -1
            self.move_counter *= -1

class Lava(pg.sprite.Sprite): 
    def __init__(self, x, y): 
        pg.sprite.Sprite.__init__(self)
        self.image = pg.transform.scale(pg.image.load('Bilder/lava.png'), (tile_size, tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

# Lager world og player objects
player1 = Player1(tile_size * 2 + PLAYER_SIZE / 2, HEIGHT - tile_size * 2, 1, 1)
player2 = Player2(tile_size + PLAYER_SIZE / 2, HEIGHT - tile_size * 2, 0, 0)

flag1 = Flag(tile_size * 15, tile_size * 2)

enemy_group1 = pg.sprite.Group()
enemy_group2 = pg.sprite.Group()

lava_group1 = pg.sprite.Group()
lava_group2 = pg.sprite.Group()



world1 = World(world_data1)
world2 = World(world_data2)


restart_button = Button(WIDTH // 2 - 50, HEIGHT // 2, restart_img)
start_button = Button(WIDTH // 2 - 350, HEIGHT // 2, start_img)
exit_button = Button(WIDTH // 2 + 150, HEIGHT // 2, exit_img)