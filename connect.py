from numpy.typing import _128Bit
import pygame
def construct(x,y):
    global board 
    board = [[0 for i in range(y)] for j in range(x)]

def level():
    i=int(input("Enter 1 2 3 for increasing size : "))
    if(i==1):
        (row,column)=(6,7)
    elif(i==2):
        (row,column)=(8,9)
    else:
        (row,column)=(10,11)
    construct(row,column)
    return((row,column))

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
    print(x,y,posi[0],posi[1])
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
    while(not victory(player+1,posi)):
        print("Player : ",player+1)
        position=int(input("Enter Positon : "))
        if not check_legal(position):
            play(player)

        posi=insert(position-1,player)
        player=(player+1)%2  
        display()


(row,column)=level()
player=0
play(player)