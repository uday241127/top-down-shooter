import pygame
import sys

pygame.init()
w=800
h=720
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("SHOOTER")

clock=pygame.time.Clock()

run=True

class player:
    
    def __init__(self):
        self.x=400
        self.y=600
        self.radius=20
        self.speed=5
    
    def draw(self):
        pygame.draw.circle(screen,(0,0,0),(self.x,self.y),self.radius)

    def move(self,keys):
        
        if keys[pygame.K_w]:
            self.y-=self.speed
        
        if keys[pygame.K_a]:
            self.x-=self.speed
        
        if keys[pygame.K_s]:
            self.y+=self.speed
        
        if keys[pygame.K_d]:
            self.x+=self.speed

    def boundary(self):
        if self.x+self.radius>w:
            self.x=w-self.radius

        if self.x-self.radius<0:
            self.x=self.radius
        
        if self.y+self.radius>h:
            self.y=h-self.radius

        if self.y-self.radius<0:
            self.y=self.radius

class bullet:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.radius=5
        self.speed=10

        mx,my=pygame.mouse.get_pos()

        dx=mx-self.x
        dy=my-self.y
        dist=(dx**2+dy**2)**0.5
        self.dx=dx/dist
        self.dy=dy/dist

    def move(self):
        self.x+=self.dx*self.speed
        self.y+=self.dy*self.speed

    def draw(self):
        pygame.draw.circle(screen,(10,10,10),(self.x,self.y),self.radius)



p=player()
bullets=[]

while run:
    keys=pygame.key.get_pressed()
    screen.fill((0,255,0))

    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            b=bullet(p.x,p.y)
            bullets.append(b)
        if event.type==pygame.QUIT:
            run=False

    for b in bullets:
        if b.x>w or b.x<0 or b.y<0 or b.y>h:
            bullets.remove(b)
        
        b.move()
        b.draw()
    p.move(keys)
    p.draw()
    p.boundary()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
