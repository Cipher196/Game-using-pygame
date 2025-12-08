import pygame
import sys

# -------------------- SETTINGS --------------------
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# -------------------- SETUP ------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Pygame Game")
clock = pygame.time.Clock()


# ------------------- FUNCTION ------------------ 

def collide(b1,b2):
    
    if b1.x + b1.w < b2.x  or b1.x > b2.x + b2.w:
        return False
    if b1.y + b1.h < b2.y or b1.y > b2.y + b2.h:
        return False
        
    return True

def enemy_move(enemy,player):
    dx=player.x-enemy.x
    dy=player.y-enemy.y

    length=(dx**2+dy**2)**0.5
    
    if length!=0:
        dx/=length
        dy/=length

    enemy.move(dx,dy)

# -------------- CLASS ----------------- 

class block:

    def __init__(self,x,y,w,h,speed,color):
        self.x=x 
        self.y=y 
        self.w=w 
        self.h=h 
        self.speed=speed
        self.color=color

    def show(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))

    def move(self,x,y):
        self.x += x*self.speed
        self.y += y*self.speed

        for block in blocks:
            if collide(self,block):
                self.x -= x*self.speed
                self.y -= y*self.speed
                return


# -------------------- BLOCK ------------------------

player=block(SCREEN_WIDTH//2,(3*SCREEN_HEIGHT)//4,40,40,3,'blue')
enemy=block(SCREEN_WIDTH//2,SCREEN_HEIGHT//4,40,40,4,'red')

blocks=[]
# --------boreder---------- 
blocks.append(block(0,0,SCREEN_WIDTH,5,0,'grey'))
blocks.append(block(0,0,5,SCREEN_HEIGHT,0,'grey'))
blocks.append(block(0,SCREEN_HEIGHT-5,SCREEN_WIDTH,5,0,'grey'))
blocks.append(block(SCREEN_WIDTH-5,0,5,SCREEN_HEIGHT,0,'grey'))

# -----------objects---------------- 

blocks.append(block(100,100,50,150,0,'grey'))
blocks.append(block(250,200,150,50,0,'grey'))


blocks.append(block(150, 50, 100, 30, 0, 'grey'))
blocks.append(block(360, 180, 40, 120, 0, 'grey'))


blocks.append(block(200, 420, 300, 30, 0, 'grey'))
blocks.append(block(600, 250, 30, 120, 0, 'grey'))


# -------------------- GAME LOOP --------------------
running = True
while running:
    # --- Event Handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False

    # --- Update (Game Logic) ---
    # Put your update code here
    keys=pygame.key.get_pressed()

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.move(-1,0)
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.move(1,0)
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.move(0,-1)
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.move(0,1)

    # if player will collide to enemy game will stop 
    if collide(player,enemy):
        running=False

    enemy_move(enemy,player)

    # --- Draw (Render) ---
    screen.fill(WHITE)       # Clear screen
    player.show()
    enemy.show()

    for block in blocks:
        block.show()
    # Put your drawing code here

    pygame.display.flip()    # Update display
    clock.tick(FPS)          # Maintain FPS


pygame.quit()
sys.exit()