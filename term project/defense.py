import pygame
from random import *
#OGA-BY 3.0

Display_Width = 800
Display_Height = 600
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
    def __init__(self, screen, block_size, x, y, lv):
        self.x = x
        self.y = y
        self.screen = screen
        self.lv = lv
        self.hp = 10000*lv
        self.gold = 10*lv
        if lv==1:
            self.img = pygame.image.load('lv1.png')
        elif lv==2:
            self.img = pygame.image.load('lv2.png')
        elif lv==3:
            self.img = pygame.image.load('lv3.png')    
        elif lv==4:
            self.img = pygame.image.load('lv4.png')
        elif lv==5:
            self.img = pygame.image.load('lv5.png')
        elif lv==6:
            self.img = pygame.image.load('lv6.png')    
        elif lv==7:
            self.img = pygame.image.load('lv7.png')    
        elif lv==8:
            self.img = pygame.image.load('lv8.png')    
        elif lv==9:
            self.img = pygame.image.load('lv9.png')    
        else:
            self.img = pygame.image.load('lv10.png')
        self.img = pygame.transform.scale(self.img, (block_size,block_size))
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
        self.img = pygame.image.load('fire.png')
        self.img = pygame.transform.scale(self.img, (40, 40))
        self.step = 0
    def Attack(self):
        for idx, item in enumerate(enemy_list):
            if abs(item.x-self.x)+abs(item.y-self.y)<=self.range:
                item.hp-=self.attack
                myscreen.blit(self.img, (self.x-abs(item.x-self.x)/1200*self.step,self.y-abs(item.y-self.y)/1200*self.step))
                self.step+=1
                return idx
        return -1
        
        
        
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
    img1 = pygame.image.load('ground.png')
    img1 = pygame.transform.scale(img1, (40,40))
    img2 = pygame.image.load('grass.png')
    img2 = pygame.transform.scale(img2, (40,40))
    for x in range(0,15):
        for y in range(0,15):
            if map[x][y]==1:
                myscreen.blit(img1, (40*y,40*x))
            else:
                myscreen.blit(img2, (40*y,40*x))
    img3 = pygame.image.load('tower.png')
    img3 = pygame.transform.scale(img3, (40,40))
    myscreen.blit(img3, (80,160))
    
def pygame_mainloop():
    pygame.init()
    draw_map()
    step = 0
    lv = 1
    a = tower(80, 160)
    running = True
    while running:
        dt = clock.tick(60)
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
            enemy_list.append(enemy(myscreen, 40, start_x, start_y, lv))
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
    