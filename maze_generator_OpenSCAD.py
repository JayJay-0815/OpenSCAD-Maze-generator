'''
Maze generator
'''


#modules
from turtle import *
from random import *
import math

#functions
def default():
    f.write('\n module path(width,length,posx,posy,rz){')
    f.write('\n 	translate([posx,posy,1])')
    f.write('\n 	rotate([0,0,rz])')
    f.write('\n 	cube([width,length, 11.01,]);')
    f.write('\n }')


    f.write('\n//Maze')
    f.write('\ndifference(){')
    f.write('\n		cylinder(12,43,43);')
    f.write('\n 	union(){ ')
        
    f.write('\n			path(50,50,-25,-25,0);')

    f.write('\n}')
    f.write('\n}')
    
def north(width,length,x,y):#270°
    f.write('\n path({0},{1},{2},{3},270);//north'.format(width,length,x,y))

def west(width,length,x,y):# 180°
    reallength = length + width
    f.write('\n path({0},{1},{2},{3},180);//west'.format(width,reallength,x,y))

def south(width,length,x,y): # 90°
    f.write('\n path({0},{1},{2},{3},90);'.format(width,length,x,y))
    
    
def east(width,length,x,y): #0°
    f.write('\n path({0},{1},{2},{3},0);//east'.format(width,length,x,y))
            

def rect(width,length,x,y):
    turn = 0
    while (turn < 4):  #painting square
        if ( turn == 1): #90°
            south(width,length,x,y)
            
        elif ( turn == 2):#180°
            east(width,length,x,y)
            
        elif( turn == 3): #270°
            north(width,length,x,y)
            
        else: #0°
            west(width,length,x,y)
              
        #print(x,y)
        turn = turn +1  #counts turns
      
def rectgrid(width,length,x,y):

    coin = randint(0,1) #open or close path
        
    if(coin == 1 ): #close path
        west(width, length, x,y)
        print('eastWall')
                
    elif(coin == 0): #open path
        north(width, length, x,y)
        print('NorthWall')

     
def grid(width,length, generations):
    counter = 0
    while (generations > counter):
        counter = counter +1
        f.write('\n')
        f.write('\n //Maze:{0}'.format(counter))
        f.write('\n')
        for y in range (-15,20,10):
            print('----------------')
            for x in range(-15,20,10):
                rectgrid(width,length,x,y)

def debuggrid(width, length):
    for y in range (-15,20,10):
        print('----------------')
        for x in range(-15,20,10):
            fullgrid(width,length,x,y)

def fullgrid(width,length,x,y):
    
    west(width, length, x,y)
    print('eastWall')
                
    north(width, length, x,y)
    print('NorthWall')
    
#opening textfile
f=open('Test_2.scad',mode='w')

#default setting
default()

#Programm
width= 50
length = 5


#Grid
#debuggrid(2.5,10)
grid(2.5,10,1) # width,length,generations

f.write('\n //End generation----------------------------')
f.close() #closing file
