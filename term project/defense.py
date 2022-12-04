import pygame
import math
import random
#OGA-BY 3.0

Default_font = 'arial'
Display_Width = 800
Display_Height = 600
Block_Size = 40
fps = 60
life = 30
gold = 150
lv = 1
start_x = 40
start_y = 0
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
ABOVE_COLOR = (234, 236, 240)
ACTIVE_COLOR = (144, 144, 144)
INACTIVE_COLOR = (215, 215, 215)
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
    def __init__(self, lv):
        self.x = start_x
        self.y = start_y
        self.lv = lv
        self.max_hp = 50+10*(lv**2)
        self.hp = self.max_hp
        self.gold = 5
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
        pygame.draw.line(myscreen, RED, [self.x+3, self.y-3], [self.x+37-(34*(self.max_hp-self.hp)/self.max_hp), self.y-3], 2)
        myscreen.blit(self.img, (self.x,self.y))
        
        
        
        
class tower:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.num = random.randint(1, 100)
        if self.num==1:
            self.lv=4
        elif self.num<=6:
            self.lv=3
        elif self.num<=50:
            self.lv=2
        else:
            self.lv=1
        self.attack_x = x
        self.attack_y = y
        if self.lv==1:
            self.attack = 5
            self.range = 160
            self.attack_img = pygame.image.load('image/attack1.png')
            self.attack_img = pygame.transform.scale(self.attack_img, (Block_Size-20, Block_Size-20))
            self.tower_img = pygame.image.load('image/tower1.png')
            self.tower_img = pygame.transform.scale(self.tower_img, (Block_Size, Block_Size))
        elif self.lv==2:
            self.attack = 10
            self.range = 240
            self.attack_img = pygame.image.load('image/attack2.png')
            self.attack_img = pygame.transform.scale(self.attack_img, (Block_Size-20, Block_Size-20))
            self.tower_img = pygame.image.load('image/tower2.png')
            self.tower_img = pygame.transform.scale(self.tower_img, (Block_Size, Block_Size))
        elif self.lv==3:
            self.attack = 30
            self.range = 320
            self.attack_img = pygame.image.load('image/attack3.png')
            self.attack_img = pygame.transform.scale(self.attack_img, (Block_Size-20, Block_Size-20))
            self.tower_img = pygame.image.load('image/tower3.png')
            self.tower_img = pygame.transform.scale(self.tower_img, (Block_Size, Block_Size))
        else:
            self.attack = 50
            self.range = 1000
            self.attack_img = pygame.image.load('image/attack4.png')
            self.attack_img = pygame.transform.scale(self.attack_img, (Block_Size, Block_Size))
            self.tower_img = pygame.image.load('image/tower4.png')
            self.tower_img = pygame.transform.scale(self.tower_img, (Block_Size, Block_Size))
        self.step = 0
        self.target = enemy(1)
    def Attack(self):
        for idx, item in enumerate(enemy_list):
            if abs(item.x-self.x)+abs(item.y-self.y)<=self.range:
                if self.target != item:
                    self.step=0
                self.target=item
                myscreen.blit(self.attack_img, (self.attack_x, self.attack_y))
                self.attack_x = self.x+(item.x-self.x)/fps*self.step*2
                self.attack_y = self.y+(item.y-self.y)/fps*self.step*2
                self.step+=1
                if math.sqrt((item.x-self.attack_x)**2+(item.y-self.attack_y)**2)<4:
                    self.step=0
                    self.attack_x = self.x
                    self.attack_y = self.y
                    item.hp-=self.attack
                return idx
        return -1
        

class button:
    def __init__(self, pos, size, name, color = BLACK):
        FONT = pygame.font.SysFont(Default_font, 20)
        self.text = FONT.render(name, True, color)
        self.text_rect = self.text.get_rect(center=pos)
        self.rect = pygame.Rect(0, 0, *size)
        self.rect.center = pos
        self.color = INACTIVE_COLOR
    def draw(self):
        pygame.draw.rect(myscreen, self.color, self.rect)
        myscreen.blit(self.text, self.text_rect)
    def above(self):
        self.color = ABOVE_COLOR
    def active(self):
        self.color = ACTIVE_COLOR
    def inactive(self):
        self.color = INACTIVE_COLOR
        
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
map_tower = [[0,1,0,1,1,1,0,1,1,1,0,1,1,1,0],
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
    myscreen.fill((125, 125, 125))
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
    for x in range(0, len(tower_list)):
        myscreen.blit(tower_list[x].tower_img, (tower_list[x].x,tower_list[x].y))
    heart = pygame.image.load('image/heart.png')
    heart = pygame.transform.scale(heart, (Block_Size,Block_Size))
    myscreen.blit(heart, (600, 0))
    coin = pygame.image.load('image/coin.png')
    coin = pygame.transform.scale(coin, (Block_Size-15,Block_Size-15))
    myscreen.blit(coin, (705, 6))
    myscreen.blit(coin, (745, 109))
    myscreen.blit(coin, (745, 179))
    FONT = pygame.font.SysFont(Default_font, 25)
    Life = FONT.render(str(life), True, BLACK)
    myscreen.blit(Life, (642, 4))
    Gold = FONT.render(str(gold), True, BLACK)
    myscreen.blit(Gold, (740, 4))
    Stage = FONT.render('Stage : '+str(lv), True, BLACK)
    myscreen.blit(Stage, (650, 50))
    Text1 = FONT.render('50', True, RED)
    myscreen.blit(Text1, (710, 107))
    Text2 = FONT.render('25', True, BLUE)
    myscreen.blit(Text2, (710, 177))
    tower_img1 = pygame.image.load('image/tower1.png')
    tower_img1 = pygame.transform.scale(tower_img1, (Block_Size, Block_Size))
    tower_img2 = pygame.image.load('image/tower2.png')
    tower_img2 = pygame.transform.scale(tower_img2, (Block_Size, Block_Size))
    tower_img3 = pygame.image.load('image/tower3.png')
    tower_img3 = pygame.transform.scale(tower_img3, (Block_Size, Block_Size))
    tower_img4 = pygame.image.load('image/tower4.png')
    tower_img4 = pygame.transform.scale(tower_img4, (Block_Size, Block_Size))
    att_img = pygame.image.load('image/att.png')
    att_img = pygame.transform.scale(att_img, (Block_Size-20, Block_Size-20))
    range_img = pygame.image.load('image/range.png')
    range_img = pygame.transform.scale(range_img, (Block_Size-20, Block_Size-20))
    myscreen.blit(tower_img1, (605, 300))
    myscreen.blit(tower_img2, (605, 380))
    myscreen.blit(tower_img3, (605, 460))
    myscreen.blit(tower_img4, (605, 540))
    myscreen.blit(att_img, (655, 310))
    myscreen.blit(att_img, (655, 390))
    myscreen.blit(att_img, (655, 470))
    myscreen.blit(att_img, (655, 550))
    myscreen.blit(range_img, (730, 310))
    myscreen.blit(range_img, (730, 390))
    myscreen.blit(range_img, (730, 470))
    myscreen.blit(range_img, (730, 550))
    
def find_tower(x, y):
    for idx in range(len(tower_list)):
        if tower_list[idx].x==(x//40*40) and tower_list[idx].y==(y//40*40):
            return idx
    return -1    

def pygame_mainloop():
    pygame.init()
    pygame.display.set_caption("Random Defense Game")
    draw_map()
    global life
    global gold
    global lv
    step = 0
    Button1 = button((650, 120), (80, 40), 'Buy')
    Button2 = button((650, 190), (80, 40), 'Sell')
    Button3 = button((650, 260), (80, 40), 'Cancel')
    running = True
    buy = False
    sell = False
    cancel = True
    while running:
        dt = clock.tick(fps)
        remove = 0
        for event in pygame.event.get():
            xpos, ypos = pygame.mouse.get_pos()
            if event.type==pygame.QUIT:
                running=False
            if life<=0:
                running=False
                if running==False:
                    break
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and buy and not sell:
                if xpos<=600 and ypos<=600 and map_tower[ypos//40][xpos//40]==0:
                    buy=False
                    tower_list.append(tower(xpos//40*40, ypos//40*40))
                    map_tower[ypos//40][xpos//40]=2
                    gold-=50
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and not buy and sell:
                if xpos<=600 and ypos<=600 and map_tower[ypos//40][xpos//40]==2:
                    sell=False
                    tower_list.pop(find_tower(xpos, ypos))
                    map_tower[ypos//40][xpos//40]=0
                    gold+=25
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and not buy and not sell:
                if Button1.rect.collidepoint(event.pos):
                    Button1.active()
                    buy=True
                elif Button2.rect.collidepoint(event.pos):
                    Button2.active()
                    sell=True     
            elif Button1.rect.collidepoint((xpos, ypos)):
                Button1.above()
            elif Button2.rect.collidepoint((xpos, ypos)):
                Button2.above()
            elif Button3.rect.collidepoint((xpos, ypos)):
                Button3.above()
            else:
                Button1.inactive()
                Button2.inactive()
                Button3.inactive()
        draw_map()
        Button1.draw()
        Button2.draw()
        Button3.draw()
        step+=1
        if step<=10*fps:
            pass
        elif step<=30*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
        elif step<=50*fps:
            if step==50*fps:
                lv+=1
        elif step<=70*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
        elif step<=90*fps:
            if step==90*fps:
                lv+=1
        elif step<=110*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
        elif step<=130*fps:
            if step==130*fps:
                lv+=1
        elif step<=150*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
        elif step<=170*fps:
            if step==170*fps:
                lv+=1
        elif step<=190*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
        elif step<=210*fps:
            if step==210*fps:
                lv+=1
        elif step<=230*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
        elif step<=250*fps:
            if step==250*fps:
                lv+=1
        elif step<=270*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
        elif step<=290*fps:
            if step==290*fps:
                lv+=1
        elif step<=310*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv)) 
        elif step<=330*fps:
            if step==330*fps:
                lv+=1
        elif step<=350*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
        elif step<=370*fps:
            if step==370*fps:
                lv+=1
        elif step<=390*fps:
            if step%fps==0:
                enemy_list.append(enemy(lv))
            
        for idx in range(len(enemy_list)):
            enemy_list[idx-remove].step+=1
            if enemy_list[idx-remove].step==len(way): # 적이 endline에 도착
                enemy_list.pop(0)
                remove+=1
                life-=1
            else:
                enemy_list[idx-remove].Draw()    
        for x in range(0, len(tower_list)):
            index=tower_list[x].Attack()
            if index!=-1 and enemy_list[index].hp<=0:
                gold+=enemy_list[index].gold
                enemy_list.pop(index)
                remove+=1
        pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":
    pygame_mainloop()
