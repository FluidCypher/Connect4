import pygame
import sys
def construct(x,y):
    global board 
    board = [[0 for i in range(y)] for j in range(x)]

def tie():
    if 0 in board[0]:
        return(False)
    return(True)
def level():
    i=int(input())
    if(i==1):
        (row,column)=(6,7)
    elif(i==2):
        (row,column)=(8,9)
    else:
        (row,column)=(10,11)
    construct(row,column)
    return((row,column))

def draw():
    pygame.display.set_caption('Connect 4')
    for i in range(row):
        for j in range(column):
            pygame.draw.rect(screen,(0,0,200),(j*size,i*size+size,size,size))
            if board[i][j]==0:
                pygame.draw.circle(screen,(0,0,0),(int((j+0.5)*size),int((i+1.5)*size)),radius)
            elif board[i][j]==1:
                pygame.draw.circle(screen,(200,0,0),(int((j+0.5)*size),int((i+1.5)*size)),radius)
            else :
                pygame.draw.circle(screen,(200,0,200),(int((j+0.5)*size),int((i+1.5)*size)),radius)
    pygame.display.update()

def display():
    for i in board:
        for j in i:
            print(j,end='  ')
        print()

def check_legal(y):
    if(board[0][y-1]==0):
        return(True)
    else:
        print("Overflow")
        return(False)

def insert(position,player):
    for i in range(row-1,-1,-1):
        if board[i][position]==0.0:
            board[i][position]=player+1
            break
    return((i,position))

def horizontal(player,posi):
    s=''
    for i in board[posi[0]]:
        s+=str(i)
    if str(player)*4 in s:
        return(True)
    return(False)

def vertical(player,posi):
    s=''
    for i in board:
        s+=str(i[posi[1]])
    if str(player)*4 in s:
        return(True)
    return(False)

def ldiagonal(player,posi):
    s=''
    x,y=posi[0]-min(posi[0],posi[1]),posi[1]-min(posi[0],posi[1])
    while(x<row and y<column):
        s+=str(board[x][y])
        x+=1
        y+=1
    if str(player)*4 in s:
        return(True)
    return(False)    

def rdiagonal(player,posi):
    s=''
    x,y=posi[0],posi[1]
    while(x<row-1 and y>0):
        x+=1
        y-=1
    while(x>0 and y<column-1):
        s+=str(board[x][y])
        x-=1
        y+=1
    if str(player)*4 in s:
        return(True)
    return(False)    

def victory(player,posi):
    if posi==tuple():
        return(False)
    return(horizontal(3-player,posi) or vertical(3-player,posi) or ldiagonal(3-player,posi) or rdiagonal(3-player,posi))

def play(player):
    posi=tuple()
    while(not victory(player+1,posi) and not tie()):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen,(0,0,0),(0,0,size*row+size,size))
                if player == 0:
                    pygame.draw.circle(screen,(200,0,0),(event.pos[0],size//2),radius)
                elif player == 1:
                    pygame.draw.circle(screen,(200,0,200),(event.pos[0],size//2),radius)
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                position=event.pos[0]//size+1
                if not check_legal(position):
                    play(player)

                posi=insert(position-1,player)
                player=(player+1)%2  
                display()
                draw()


pygame.init()
size=75
radius=size//2-5
screen = pygame.display.set_mode((300,100))
myfont=pygame.font.SysFont("monospace", 50)
a=1
while (a==1):
    for event in pygame.event.get():
        pygame.display.set_caption('Choose Level')
        pygame.draw.rect(screen,(200,0,0),(0,0,100,100))
        pygame.draw.rect(screen,(0,200,0),(100,0,100,100))
        pygame.draw.rect(screen,(0,0,200),(200,0,100,100))
        label=myfont.render("1", True, (0,200,0))
        screen.blit(label,(35,25))
        label=myfont.render("2", True, (0,0,200))
        screen.blit(label,(135,25))
        label=myfont.render("3", True, (200,0,0))
        screen.blit(label,(235,25))
        pygame.display.update()
        if event.type == pygame.QUIT:
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            i=event.pos[0]//100
            if(i==0):
                (row,column)=(6,7)
            elif(i==1):
                (row,column)=(8,9)
            else:
                (row,column)=(10,11)
            construct(row,column)
            a=2
screen = pygame.display.set_mode((column*size,(row+1)*size))
draw()
player=0
play(player)
label=myfont.render("Game Over",1,(0,200,0))
screen.blit(label,((column*size)//4,0))
pygame.display.update()
pygame.time.wait(2000)
