import pygame
import sys
import random

pygame.init()
w=800
h=720
screen=pygame.display.set_mode((w,h))
pygame.display.set_caption("SHOOTER")
font=pygame.font.SysFont("Arial",40)

clock=pygame.time.Clock()

run=True
score=0

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

class enemy:
    def __init__(self):

        while True:
            self.x=random.randint(100,700)
            self.y=random.randint(100,620)
            self.speed=2
            self.radius=10
            dx=p.x-self.x
            dy=p.y-self.y
            dist=(dx**2+dy**2)**0.5

            if dist>200:
                break

    def draw(self):
        pygame.draw.circle(screen,(255,0,0),(self.x,self.y),self.radius)

    def move(self,p):
        dx=p.x-self.x
        dy=p.y-self.y
        dist=(dx**2+dy**2)**0.5
        self.dx=dx/dist
        self.dy=dy/dist
        self.x+=self.speed*self.dx
        self.y+=self.speed*self.dy
    
class collision:
    def __init__(self):
        return
    
    def enemy_bullet(self,p,bullets,enemies):
        for b in bullets:
            for e in enemies:
                dx=b.x-e.x
                dy=b.y-e.y
                dist=(dx**2+dy**2)**0.5
                if dist<=b.radius+e.radius:
                    bullets.remove(b)
                    enemies.remove(e)
                    p.radius+=e.radius
                    return 1
        return 0
    
    def enemy_player(self,p,enemies):
        for e in enemies:
            dx=p.x-e.x
            dy=p.y-e.y
            dist=(dx**2+dy**2)**0.5
            if dist<=p.radius+e.radius:
                enemies.remove(e)
                p.radius-=e.radius
                return 1
        return 0

class g_over:
    def __init__(self):
        return

    def over(self,p):
        if p.radius<=0:
            game_over=font.render("GAME OVER",True,(0,0,0))
            screen.blit(game_over,(300,300))
            screen.blit(sc,(300,340))
            pygame.display.update()
            pygame.time.delay(2400)
            return False
        return True           

p=player()
bullets=[]
enemies=[]
c=collision()
enemy_count=3

for i in range(3):
    e=enemy()
    enemies.append(e)

while run:
    keys=pygame.key.get_pressed()
    screen.fill((0,255,0))

    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            b=bullet(p.x,p.y)
            bullets.append(b)
        if event.type==pygame.QUIT:
            run=False

    g=g_over()
    run=g.over(p)

    p.move(keys)
    p.draw()
    p.boundary()

    for b in bullets:
        if b.x>w or b.x<0 or b.y<0 or b.y>h:
            bullets.remove(b)
        
        b.move()
        b.draw()
    
    for e in enemies:
        e.draw()
        e.move(p)
        
    score+=c.enemy_bullet(p,bullets,enemies)
    c.enemy_player(p,enemies)

    if not enemies:
        enemy_count+=1
        for i in range(enemy_count):
            e=enemy()
            enemies.append(e)

    sc=font.render(f"SCORE:{score}",True,(0,0,0))
    screen.blit(sc,(10,10))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
