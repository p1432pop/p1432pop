import pygame
from random import *
#OGA-BY 3.0

Display_Width = 800
Display_Height = 600
Block_Size = 40
fps = 60
start_x = 40
start_y = 0
RED = (255, 0, 0)
myscreen = pygame.display.set_mode((Display_Width, Display_Height))
clock = pygame.time.Clock()
enemy_list = []
tower_list = []
way = []
for idx in range(0,560):
    way.append([0, 1])
for idx in range(0, 80):
    way.append([1, 0])
for idx in range(0,560):
    way.append([0, -1])
for idx in range(0, 80):
    way.append([1, 0])
for idx in range(0,560):
    way.append([0, 1])
for idx in range(0, 80):
    way.append([1, 0])
for idx in range(0,560):
    way.append([0, -1])
for idx in range(0, 80):
    way.append([1, 0])
for idx in range(0,560):
    way.append([0, 1])
for idx in range(0, 80):
    way.append([1, 0])
for idx in range(0,560):
    way.append([0, -1])
for idx in range(0, 80):
    way.append([1, 0])  
for idx in range(0,560):
    way.append([0, 1])    
    
    
class enemy:
    def __init__(self, screen, x, y, lv):
        self.x = x
        self.y = y
        self.screen = screen
        self.lv = lv
        self.hp = 10000*lv
        self.gold = 10*lv
        if lv==1:
            self.img = pygame.image.load('image/lv1.png')
        elif lv==2:
            self.img = pygame.image.load('image/lv2.png')
        elif lv==3:
            self.img = pygame.image.load('image/lv3.png')    
        elif lv==4:
            self.img = pygame.image.load('image/lv4.png')
        elif lv==5:
            self.img = pygame.image.load('image/lv5.png')
        elif lv==6:
            self.img = pygame.image.load('image/lv6.png')    
        elif lv==7:
            self.img = pygame.image.load('image/lv7.png')    
        elif lv==8:
            self.img = pygame.image.load('image/lv8.png')    
        elif lv==9:
            self.img = pygame.image.load('image/lv9.png')    
        else:
            self.img = pygame.image.load('image/lv10.png')
        self.img = pygame.transform.scale(self.img, (Block_Size,Block_Size))
        self.step = 0
        
    def Draw(self):
        self.x+=way[self.step][0]
        self.y+=way[self.step][1]
        myscreen.blit(self.img, (self.x,self.y))
        
        
        
        
class tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attack = 10
        self.range = 80
        self.img = pygame.image.load('image/fire.png')
        self.img = pygame.transform.scale(self.img, (Block_Size, Block_Size))
        self.step = 0
    def Attack(self):
        for idx, item in enumerate(enemy_list):
            if abs(item.x-self.x)+abs(item.y-self.y)<=self.range:
                item.hp-=self.attack
                myscreen.blit(self.img, (self.x-abs(item.x-self.x)/1200*self.step,self.y-abs(item.y-self.y)/1200*self.step))
                self.step+=1
                return idx
        return -1
        
class user:
    def __init__(self):
        self.life = 30
        self.gold = 50
        
        
map = [[0,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
       [0,1,1,1,0,1,1,1,0,1,1,1,0,1,0]]

def draw_map():
    myscreen.fill((15, 50, 10))
    ground = pygame.image.load('image/ground.png')
    ground = pygame.transform.scale(ground, (Block_Size,Block_Size))
    grass = pygame.image.load('image/grass.png')
    grass = pygame.transform.scale(grass, (Block_Size,Block_Size))
    for x in range(0,15):
        for y in range(0,15):
            if map[x][y]==1:
                myscreen.blit(ground, (Block_Size*y,Block_Size*x))
            else:
                myscreen.blit(grass, (Block_Size*y,Block_Size*x))
    img3 = pygame.image.load('image/tower.png')
    img3 = pygame.transform.scale(img3, (Block_Size,Block_Size))
    myscreen.blit(img3, (80,160))
    
def pygame_mainloop():
    pygame.init()
    draw_map()
    step = 0
    lv = 1
    a = tower(80, 160)
    running = True
    while running:
        dt = clock.tick(fps)
        remove = 0
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if len(enemy_list)>=1:
                        enemy_list.pop(0)
        draw_map()
        step+=1
        if step%60==0:
            enemy_list.append(enemy(myscreen, start_x, start_y, lv))
        if step%600==0:
            lv+=1
        for idx in range(len(enemy_list)):
            enemy_list[idx-remove].step+=1
            if enemy_list[idx-remove].step==len(way):
                enemy_list.pop(0)
                remove+=1
            else:
                enemy_list[idx-remove].Draw()    
                index = a.Attack()
                if index!=-1 and enemy_list[index].hp<=0:
                    enemy_list.pop(0)
                    remove+=1
        pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":
    pygame_mainloop()
    
