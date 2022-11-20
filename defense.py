import pygame
from random import *
BLOCK_SIZE = 32
Display_Width = 600
Display_Height = 600
class enemy:
    def __init__(self, screen, block_size, start, x, y, lv):
        self.__x = x
        self.__y = y
        self.__screen = screen
        self.__lv = lv
        self.__hp = 5*lv
        self.__gold = 10*lv

class tower:
    def __init__(self, screen, block_size, x, y):
        self.__rank = randint(1,6)
        self.__range = __rank
    def find_enemy:
        for dis in range(1:__range):
            
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
def pygame_mainloop():
    pygame.init()
    
    myscreen = pygame.display.set_mode((Display_Width, Display_Height))
    myscreen.fill((15, 50, 10))
    img = pygame.image.load('block.svg')
    img = pygame.transform.scale(img, (40,40))
    myscreen.blit(img, (0,0))
    for x in range(0,15):
        for y in range(0,15):
            if map[x][y]==0:
                myscreen.blit(img, (40*y,40*x))
                
    running = True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pygame.display.update()
    pygame.quit()
    
if __name__ == "__main__":
    pygame_mainloop()
    
