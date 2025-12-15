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

def check_enemy_collision():

    player.w = player.Size_Tiles
    player.h = player.Size_Tiles
    enemy.w = enemy.Size_Tiles
    enemy.h = enemy.Size_Tiles

    if not(player.x+player.w<enemy.x or player.x>enemy.x+enemy.w or player.y+player.h<enemy.y or player.y>enemy.y+enemy.h):
        global running
        running=False

# Applying Dijkstra 

import heapq as hq

def astar(start,end):
    
    open_set=[]
    hq.heappush(open_set,(h(start),start))
    
    came_from={}

    g_score={}
    g_score[start]=0

    while open_set:
        f_curr,curr=hq.heappop(open_set)

        if curr==end:
            return remake_path(came_from,curr)
        
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        for direction in directions:
            near=(curr[0]+direction[0],curr[1]+direction[1])
            if not check_all_corner(near[0],near[1],enemy.Size_Tiles,enemy.Size_Tiles):
                continue

            new_g_score=g_score[curr]+1
            if near not in g_score or new_g_score<g_score[near]:

                came_from[near]=curr
                g_score[near]=new_g_score
                new_f_score=new_g_score+h(near)

                if near not in open_set:
                    hq.heappush(open_set,(new_f_score,near))

    return None

def h(node):
    return abs(node[0]-player.x)+abs(node[1]-player.y)

def remake_path(came_from,curr):
    total_path=[curr]
    while curr in came_from:
        curr=came_from[curr]
        total_path.append(curr)
    total_path.reverse()
    return total_path[2]


def move_enemy():  

    next_pos=astar((int(enemy.x),int(enemy.y)),(int(player.x),int(player.y)))

    if next_pos :

        target_x,target_y=next_pos

        dx=target_x-enemy.x
        dy=target_y-enemy.y

        move_enemy_to(dx,dy)

    else:

        dx=player.x-enemy.x
        dy=player.y-enemy.y

        move_enemy_to(dx,dy)
        
def move_enemy_to(dx,dy):
    
    if dx<0:
        dx=-1
    if dx>0:
        dx=1
    if dy<0:
        dy=-1
    if dy>0:
        dy=1

    enemy.move(dx,dy)

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
        