import pygame
import numpy
def construct(x,y):
    global board 
    board = numpy.zeros((x,y))

def level():
    i=int(input("Enter 1 2 3 for increasing size : "))
    if(i==1):
        (row,column)=(4,5)
    elif(i==2):
        (row,column)=(6,7)
    else:
        (row,column)=(8,9)
    construct(row,column)
    return((row,column))

def check_legal(y):
    if(board[0,y]==0):
        return(True)
    else:
        return(False)

def insert(column,x):
    for i in range(column):
        if (board[i,column]!=0):
            board[i-1,column]=x

def victory():
    return(True)

(row,column)=level()

player=0
while(victory()):
    continue
