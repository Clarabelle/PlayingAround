import pygame
pygame.init()
#dis=pygame.display.set_mode((800,600))


num=0
import random
black=(0,0,0)
otra=(59,67,196)
gameClose=False

dis=pygame.display.set_mode((1000,750))

while not gameClose:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameClose=True
    pygame.draw.rect(dis,otra,[0,0,1000,750])
    
    while num<=64:
        num+=1
        foodx=round(random.randrange(0,40))*25
        foody=round(random.randrange(0,30))*25
        print("("+str(foodx)+","+str(foody)+")")
        pygame.draw.rect(dis,black,[foodx,foody,25,25])
        pygame.display.update()

    pygame.display.update()

pygame.quit()
