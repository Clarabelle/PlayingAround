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





"""

import os

print('getcwd:      ', os.getcwd())
print('__file__:    ', __file__)






print('[set target path 1]')
target_path_1 = os.path.join(os.path.dirname(__file__), 'target_1.txt')

print('target_path_1: ', target_path_1)

print('read target file:')
with open(target_path_1) as f:
    print(f.read())
"""

"""
print("Start")
f=__file__
print(f)
print("new f:")
print(repr(f.rstrip("\\Starts.py")))
f=repr(f.rstrip("\\Starts.py"))
print("new f fo su:")
print(f)
"""



'''
x=int(input("x: "))
y=int(input("y: "))

if (2*x+y==15 and 2*x+2*y==18) or (3*x+-y==18 and 7*y==-x):
    print("("+str(x)+", "+str(y)+") is a solution to a system of equations.")
'''
'''

score=3
highScore=5

import pickle



scoreTryout=score

print("tryout:"+str(scoreTryout))

highScore=pickle.load(open("highScore.p","rb"))

print("high:"+str(highScore))

if scoreTryout >= highScore:
    highScore=scoreTryout

print("new high:"+str(highScore))

pickle.dump(highScore, open("highScore.p","wb"))

'''


#File Opener; tips on what everything can do. Probably need to import something to use it
'''
open(
    file,           # The pathname
    mode=’r’,       # The mode to open the file in
    buffering=-1,   # The buffering policy
    encoding=None,  # The encoding used for the file
    errors=None,    # How encoding/decoding errors are handled
    newline=None,   # How to identify new lines
    closefd=True,   # Whether to keep file descriptor open
    opener=None     # Using a custom opener
    )
'''


















"""
gameClose=False

while not gameClose:
    for event in pygame.event.get():
        print(event)

pygame.display.update()
pygame.quit()
quit()
"""