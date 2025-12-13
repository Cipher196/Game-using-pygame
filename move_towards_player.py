import pygame
import sys

# Settings

TILE_SIZE=20

grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],]

Screen_Width=len(grid[0])*TILE_SIZE
Screen_Height=len(grid)*TILE_SIZE

FPS=60

# Setup

pygame.init()
screen=pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Simple chase the player")
clock=pygame.time.Clock()

# Class 

class block:

    def __init__(self,x,y,Size_Tiles,speed,color):
        self.x=x
        self.y=y 
        self.Size_Tiles=Size_Tiles
        self.speed=speed
        self.color=color

    def show(self):
        pygame.draw.rect(screen,self.color,(self.x*TILE_SIZE,self.y*TILE_SIZE,TILE_SIZE*self.Size_Tiles,TILE_SIZE*self.Size_Tiles))

    def move(self,x,y):

        dx=self.x+(x*self.speed)
        dy=self.y+(y*self.speed)

        if check_all_corner(dx,dy,self.Size_Tiles,self.Size_Tiles):
            self.x=dx
            self.y=dy
            return

        if check_all_corner(dx,self.y,self.Size_Tiles,self.Size_Tiles):
            self.x=dx
            return
        
        if check_all_corner(self.x,dy,self.Size_Tiles,self.Size_Tiles):
            self.y=dy
            return

        

# Blocks 

player=block(10,5,2,0.2,'blue')
enemy=block(20,20,2,0.2,'red')

# functions 

def show_screen():

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                pygame.draw.rect(screen,'grey',(j*TILE_SIZE,i*TILE_SIZE,TILE_SIZE,TILE_SIZE))
            else :
                pygame.draw.rect(screen,'white',(j*TILE_SIZE,i*TILE_SIZE,TILE_SIZE,TILE_SIZE))


def check_corner(x,y):
    if grid[int(y)][int(x)]==0:
        return True
    else :
        return False
    
def check_all_corner(x,y,w,h):
    return check_corner(x,y) and check_corner(x+w,y) and check_corner(x,y+h) and check_corner(x+w,y+h)

def move_enemy():

    dx=player.x-enemy.x
    dy=player.y-enemy.y

    dist=(dx**2+dy**2)**0.5

    if dist!=0:
        dx/=dist
        dy/=dist

    enemy.move(dx,dy)

def check_enemy_collision():

    player.w = player.Size_Tiles
    player.h = player.Size_Tiles
    enemy.w = enemy.Size_Tiles
    enemy.h = enemy.Size_Tiles

    if not(player.x+player.w<enemy.x or player.x>enemy.x+enemy.w or player.y+player.h<enemy.y or player.y>enemy.y+enemy.h):
        global running
        running=False
        

# Game Loop 

running=True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    # Game Logic 
    keys=pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(-1,0)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move(1,0)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move(0,-1)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move(0,1)

    move_enemy()

    check_enemy_collision()

    # Draw 
    show_screen()
    player.show()
    enemy.show()


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
        