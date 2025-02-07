import pygame
import time
import random
import numpy
import math
import queue
import sys

#sys.setrecursionlimit(2000)

from pygame.locals import *
#from genetic import*

pygame.init()
pygame.font.init()

# commands needed:
#   pip install pygame
#   pip install numpy
running = True

#define colors
BLACK = (0,0,0)
WHITE = (255,255,255) 
RED = (193,0,0)
GREEN = (0,200,100)
BLUE = (0,0,255)
PURPLE = (0,0,128)
PINK = (255,6,131)
ORANGE = (217,108,0)
LPURPLE = (128,128,255)
LBLUE = (111,172,255)
YELLOW = (239,163,9)
DGREEN = (0,80,0)
GOLD = (220,200,10)
TEAL = (0,162,232)


font = pygame.font.SysFont('Comic Sans', 50)

zero = font.render('0', False, GOLD) 
one = font.render('1', False, BLUE) 
two = font.render('2', False, GREEN)
three = font.render('3', False, PURPLE)
four = font.render('4', False, RED)
five = font.render('5', False, LPURPLE)
six = font.render('6', False, ORANGE)
seven = font.render('7', False, PINK)
eight = font.render('8', False, LBLUE)
nine = font.render('9', False, YELLOW)
ten = font.render('10', False, DGREEN)
eleven = font.render('11', False, TEAL)
twelve = font.render('12', False, BLACK)

# Arrsize
#arrsize = 11  #can change to 5, 7, 9, or 11
#___________

running = True
hill = True
large = False

#print(graph)

while (running):
    font = pygame.font.SysFont('Times New Roman', 30)
    temp = pygame.display.set_mode((250,190))
    temp.fill(WHITE)
    temp.blit(font.render('Select Grid Size', False, BLACK),(0,0))
    font = pygame.font.SysFont('Times New Roman', 22)
    temp.blit(font.render('Enter letter of your choice', False, BLACK),(0,40))
    temp.blit(font.render('a) 5x5', False, BLACK),(2,65))
    temp.blit(font.render('b) 7x7', False, BLACK),(2,90))
    temp.blit(font.render('c) 9x9', False, BLACK),(2,115))
    temp.blit(font.render('d) 11x11', False, BLACK),(2,140))
    temp.blit(font.render('e) 31x31', False, BLACK),(2,165))
    pygame.display.update()

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                arrsize=5
                running = False
            if event.key == pygame.K_b:
                arrsize=7
                running = False
            if event.key == pygame.K_c:
                arrsize=9
                running = False
            if event.key == pygame.K_d:
                arrsize=11
                running = False
            if event.key == pygame.K_e: # 31 is largest
                large = True
                arrsize=31
                running = False
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

font = pygame.font.SysFont('Comic Sans', 50)

running = True
#screen size definitions
screen1 = None
if arrsize == 5 or arrsize == 3:
    screen1 = 510,320 #5x5
if arrsize == 7:
    screen1 = 710,420 #7x7
if arrsize == 9:
    screen1 = 910,520 #9x9
if arrsize == 11:
    screen1 = 1110,620 #11x11

if (screen1 is not None):
    screen = pygame.display.set_mode(screen1)
elif (arrsize > 11):
    screen1 = 1900,1000
    screen = pygame.display.set_mode(screen1)

runBFS = False
runHill = False
runAstar = False
runGA = False
compare = False
gaBfs = False
gaAstar = False

if (arrsize <12): 
    while (running):
        font = pygame.font.SysFont('Times New Roman', 30)
        temp = pygame.display.set_mode((250,190))
        temp.fill(WHITE)
        temp.blit(font.render('Pick Search', False, BLACK),(0,0))
        font = pygame.font.SysFont('Times New Roman', 22)
        temp.blit(font.render('Enter letter of your choice', False, BLACK),(0,40))
        temp.blit(font.render('a) Breadth First Search', False, BLACK),(2,65))
        temp.blit(font.render('b) Hill Climbing (65x)', False, BLACK),(2,90))
        temp.blit(font.render('c) A* Search', False, BLACK),(2,115))
        temp.blit(font.render('d) Genetic Algorithm', False, BLACK),(2,140))
        temp.blit(font.render('e) Compare BFS and Astar', False, BLACK),(2,165))
        #temp.blit(font.render('e) 31x31', False, BLACK),(2,165))
        pygame.display.update()

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    runBFS = True
                    running = False
                if event.key == pygame.K_b:
                    runHill = True
                    running = False
                if event.key == pygame.K_c:
                    runAstar = True
                    running = False
                if event.key == pygame.K_d:
                    runGA = True
                    running = False
                if event.key == pygame.K_e:
                    compare = True
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
elif (large == True): # big array, better to do simple a search
    while (running):
        font = pygame.font.SysFont('Times New Roman', 30)
        temp = pygame.display.set_mode((250,190))
        temp.fill(WHITE)
        temp.blit(font.render('Pick Search', False, BLACK),(0,0))
        font = pygame.font.SysFont('Times New Roman', 22)
        temp.blit(font.render('Enter letter of your choice', False, BLACK),(0,40))
        temp.blit(font.render('a) A* Search', False, BLACK),(2,65))
        temp.blit(font.render('b) Breadth First Search', False, BLACK),(2,90))
        pygame.display.update()

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    runAstar = True
                    running = False
                if event.key == pygame.K_b:
                    runBFS = True
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


running = True
if runGA == True:
    while running:
        font = pygame.font.SysFont('Times New Roman', 30)
        temp = pygame.display.set_mode((250,190))
        temp.fill(WHITE)
        temp.blit(font.render('Pick Search', False, BLACK),(0,0))
        font = pygame.font.SysFont('Times New Roman', 22)
        temp.blit(font.render('Enter letter of your choice', False, BLACK),(0,40))
        temp.blit(font.render('a) A* Search', False, BLACK),(2,65))
        temp.blit(font.render('b) Breadth First Search', False, BLACK),(2,90))
        pygame.display.update()

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    gaBfs = False
                    gaAstar = True
                    running = False
                if event.key == pygame.K_b:
                    gaBfs = True
                    gaAstar = False
                    running = False
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def randGrid(n):
    tmpgrid = numpy.full([arrsize, arrsize],-1,dtype = int)
    for row in range(n):
        for col in range(n):
            num = random.randint(1,arrsize-1)
            while ( (row+num>n and row-num<0 and col+num>n and col-num<0) ) : #we need a new number
                num = random.randint(1,arrsize-1-1) 
            tmpgrid[row,col] = num
    tmpgrid[n-1][n-1]=0
    return tmpgrid

def Draw(n,grid,mymoves,check):
    screen = pygame.display.set_mode(screen1)

    while True:

        keys = pygame.key.get_pressed()

        if (large == False) : # just 5,7,9,11
            for row in range(n):
                for col in range(n*2):
                    if col < n:
                        pygame.draw.rect(screen, WHITE, [(50)*col+5,(50)*row+5,45,45])
                    else:
                        pygame.draw.rect(screen, WHITE, [(50)*col+10,(50)*row+5,45,45])
        else:
             for row in range(n):
                for col in range(n*2):
                    if col < n:
                        pygame.draw.rect(screen, WHITE, [(30)*col+5,(30)*row+5,25,25])
                    else:
                        pygame.draw.rect(screen, WHITE, [(30)*col+10,(30)*row+5,25,25])
        break

    pygame.display.update()
    if (large == False):
        x = 19
        y = 12
    else:
        x = 12
        y = 7
    
    for row in range(arrsize):
        for col in range(arrsize):
            if (col%arrsize == 0 and row != 0 and large == False):
                y+=50
                x=19     
                
            elif (col%arrsize == 0 and row!= 0 and large == True):
                y+=30
                x=12   

            # IMPORTANT
            #num = grid[row,col]             
            #screen.blit(font.render(str(num), False, BLACK),(x,y))
            #x+=50
            if (large == False):
                if grid[row,col] == 0:
                    screen.blit(zero,(x,y))
                elif grid[row,col] == 1:
                    screen.blit(one,(x,y))
                    x+=50
                elif grid[row,col] == 2:
                    screen.blit(two,(x,y))
                    x+=50
                elif grid[row,col] == 3:
                    screen.blit(three,(x,y))
                    x+=50
                elif grid[row,col] == 4:
                    screen.blit(four,(x,y))
                    x+=50
                elif grid[row,col] == 5:
                    screen.blit(five,(x,y))
                    x+=50
                elif grid[row,col] == 6:
                    screen.blit(six,(x,y))
                    x+=50
                elif grid[row,col] == 7:
                    screen.blit(seven,(x,y))
                    x+=50
                elif grid[row,col] == 8:
                    screen.blit(eight,(x,y))
                    x+=50
                elif grid[row,col] == 9:
                    screen.blit(nine,(x,y))
                    x+=50
                elif grid[row,col] == 10:
                    screen.blit(ten,(x-10,y))
                    x+=50
                elif grid[row,col] == 11:
                    screen.blit(eleven,(x-10,y))
                    x+=50
                elif grid[row,col] == 12:
                    screen.blit(twelve,(x-10,y))
                    x+=50
              
            else:
                font = pygame.font.SysFont('Comic Sans', 32)
                num = grid[row,col]             
                if (num <10):
                    screen.blit(font.render(str(num), False, BLACK),(x,y))
                else:
                    if (row == arrsize-1 and col == arrsize-1): #make bottom right gold
                        #print("here")
                        screen.blit(font.render(str(num), False, GOLD),(x,y))
                    else:
                        screen.blit(font.render(str(num), False, BLACK),(x-6,y))
                x+=30
                
            
        
        #pygame.display.flip()
    #pygame.display.set_mode(screen1)
    font = pygame.font.SysFont('Comic Sans', 30)
    temp.blit(font.render('Press \'space\' button for solutions', False, WHITE),(0,y+40))   
    temp.blit(font.render('Press \'Esc\' button to close ', False, WHITE),(0,y+60))   
    pygame.display.flip()
    font = pygame.font.SysFont('Comic Sans', 50)

    while True: #press space to see solution
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (x %100 != 19) and large == False: x-=50 
                    drawMoves(arrsize,x,mymoves,check)
                if event.key == pygame.K_ESCAPE:
                    return
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def getEuc(cell):
    x = math.sqrt((0 - arrsize-1) ** 2 + (0 - arrsize-1) ** 2)
    return x

def getValueFunction(mymoves):
    value = 0

    if (mymoves[arrsize-1,arrsize-1])==-1:
        for row in range(arrsize):
            for col in range(arrsize):
                if mymoves[row,col] == -1:
                    value-=1
    else:
        value = mymoves[arrsize-1,arrsize-1]

    return value

def drawMoves(n,x,mymoves,check):
    #print("hi")
    #tempx = x

    if (large == False):
        x += 55
        y=12
        #print("***********************")
    else: 
        x += 6
        y = 7
   
    tempx = x
    #y = 12


    #print(mymoves)
    foundNone = False
    for row in range(arrsize):
        for col in range(arrsize):
            if mymoves is None:
                foundNone = True
                break
            if (col%arrsize == 0 and row != 0 and large == False):
                y+=50
                x=tempx    
                #print("--------------------------") 
            elif (col%arrsize == 0 and row!= 0 and large == True):
                y+=30
                x=tempx
                #print("=============================")
            # IMPORTANT
            num = mymoves[row,col]      
            if (num == -1 and check == False):
                if (large == False):
                    font = pygame.font.SysFont('Comic Sans', 50)
                    screen.blit(font.render('X', False, RED),(x-2,y))
                    #print("???????????????????????????????")
                else:
                    font = pygame.font.SysFont('Comic Sans', 32)
                    screen.blit(font.render('X', False, RED),(x-3,y))
            elif (check == True and num ==-1):
                font = pygame.font.SysFont('Comic Sans', 50)  
                if (num == -1 ):
                    screen.blit(font.render(' ', False, BLACK),(x,y-5))
            else:
                if (large == False):
                    font = pygame.font.SysFont('Comic Sans', 50)
                    if (num>9): #centerss two digit
                        screen.blit(font.render(str(num), False, BLUE),(x-12,y))
                    else:
                        screen.blit(font.render(str(num), False, BLUE),(x,y))
                      
                else:
                    font = pygame.font.SysFont('Comic Sans', 32)
                    if (num>9): #centerss two digit
                        screen.blit(font.render(str(num), False, BLUE),(x-6,y))
                    elif(x is not None):
                        screen.blit(font.render(str(num), False, BLUE),(x,y))
            
            if (large == False):
                x+=50  
                #print("****************************************************************************")
            else:
                x+=30 
        if foundNone == True:
        
            break
        #print("x",x,"y",y)
        #pygame.display.flip()
    
    if foundNone == True:
            #y+=45
            font = pygame.font.SysFont('Comic Sans', 25)
            screen.blit(font.render('NO PATH', False, RED),(screen1[0]-105,screen1[1]-65) )
            pygame.display.flip()

    else:
        y+=45
        value = getValueFunction(mymoves)
        font = pygame.font.SysFont('Comic Sans', 25)
        screen.blit(font.render('VALUE: '+str(value), False, WHITE),(x-102,y))
        pygame.display.flip()

    keys = pygame.key.get_pressed()
    
    while running: #press escape to quit
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    break
        break
        




"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
BFS Search
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def BFS(n,grid):
    # 2D array of moves
    mymoves = numpy.full([arrsize, arrsize],-1,dtype = int)

    max = 0
    c = 1
    x = 0
    y = 0

    # queue of adjacents
    q = []
    seen = []
    tagged = []

    #start at 0,0
    q.append((x,y))
    q.append((-1,-1))
    #print("1")
    
    mymoves[x,y] = 0 #first move is 0

    while q:
        
        cell = q.pop(0)

        
        if (cell not in tagged and cell != (-1,-1) ):
            seen.append(cell)
            tagged.append(cell)
        #print("2")
        if (cell[0]+grid[cell] < n and cell != (-1,-1) and (cell[0]+grid[cell],cell[1]) not in tagged): #if x postion + cell value is less than max arrsize, valid       
            q.append((cell[0]+grid[cell],cell[1]))
            if ((cell[0]+grid[cell],cell[1]) not in tagged and cell != (arrsize-1,arrsize-1)):
                mymoves[cell[0]+grid[cell],cell[1]] = c
                tagged.append((cell[0]+grid[cell],cell[1]))

        if (cell[0]-grid[cell] >= 0 and cell != (-1,-1) and (cell[0]-grid[cell],cell[1]) not in tagged):
            q.append((cell[0]-grid[cell],cell[1]))
            if ((cell[0]-grid[cell],cell[1]) not in tagged and cell != (arrsize-1,arrsize-1)):
                mymoves[cell[0]-grid[cell],cell[1]] = c
                tagged.append((cell[0]-grid[cell],cell[1]))
                

        if (cell[1]+grid[cell] < n and cell != (-1,-1) and (cell[0],cell[1]+grid[cell]) not in tagged):
            q.append((cell[0],cell[1]+grid[cell]))
            if ((cell[0],cell[1]+grid[cell]) not in tagged and cell != (arrsize-1,arrsize-1)):
                mymoves[cell[0],cell[1]+grid[cell]] = c
                tagged.append((cell[0],cell[1]+grid[cell]))

        if (cell[1]-grid[cell] >= 0 and cell != (-1,-1) and (cell[0],cell[1]-grid[cell]) not in tagged):
            q.append((cell[0],cell[1]-grid[cell]))
            if ((cell[0],cell[1]-grid[cell]) not in tagged and cell != (arrsize-1,arrsize-1)):
                mymoves[cell[0],cell[1]-grid[cell]] = c
                tagged.append((cell[0],cell[1]-grid[cell]))
         
        if (cell == (-1,-1)): # separated levels
            c+=1
            q.append((-1,-1))
            
        if (c == n*n):
            #print(q)
            break
        
    for row in range(arrsize):
        for col in range(arrsize):
            if((row,col)not in tagged):
                mymoves[row,col] = -1

    return mymoves        

allmoves = []
allpuzzles = []
def hillClimb(n):
    bestMoves = None
    bestGrid = None

    start = time.process_time()
    i = 0
    while (i < n):
        mygrid = randGrid(arrsize)
        mymoves = BFS(arrsize,mygrid)
        allmoves.append(mymoves)
        allpuzzles.append(mygrid)
        i+=1

    bestGrid = allpuzzles[0]   
    bestMoves = allmoves[0]

    
   
    for i in range(len(allmoves)):

        for row in range(arrsize):
            for col in range(arrsize) :
                if (row==arrsize-1 and col==arrsize-1):
                    #print(row,col)
                    break
                tmpCell = allpuzzles[i][row,col]
                tmpVal = allmoves[i][arrsize-1,arrsize-1]
                #print("before", tmpCell)
                num = random.randint(1,arrsize-1)
                
                while (tmpCell == num or (row+num>arrsize and row-num<0 and col+num>arrsize and col-num<0)):
                    num = random.randint(1,arrsize-1)
            
                
                allpuzzles[i][row,col] = num
                allmoves[i] = BFS(arrsize,allpuzzles[i])
                #print("yo",i,allmoves[i][arrsize-1,arrsize-1])
                if (allmoves[i][arrsize-1,arrsize-1] < tmpVal) :#revert
                    allpuzzles[i][row,col] = tmpCell
                    allmoves[i] = BFS(arrsize,allpuzzles[i])

        if (bestMoves[arrsize-1,arrsize-1] <= allmoves[i][arrsize-1,arrsize-1]):
            bestMoves = allmoves[i]
            bestGrid = allpuzzles[i]
            
        #KEEEEEEEP
        print("Iteration",i)
        print("Puzzle Value",bestMoves[arrsize-1,arrsize-1])
        print("...")
    print("Time:",time.process_time() - start)

    print("Best Grid")
    print(bestGrid)
    print("Best Moves")
    print(bestMoves)
    print("\n")
    Draw(arrsize,bestGrid,bestMoves,False)
       
#print("\nPLEASE WAIT FOR ALL ITERATIONS...\n")
#hillClimb(2)



class Node:
    def __init__(self,index):
        self.isGoal=False
        self.index=index
        self.PathfromStart=[]



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
A* Search
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def Astar(grid):
    euc = math.sqrt((0 - arrsize-1) ** 2 + (0 - arrsize-1) ** 2)
    start=Node((0,0))
    start.isStart= True
    start.isGoal = False
    neighbors=[]

    FilledList=[]
    VisitedList=[]
    PathList=[]

    goalCell = (arrsize-1,arrsize-1)
    pQ=queue.PriorityQueue()
    count=0
    pQ.put((euc,count,start))
    count+=1

    itercount =0
    while  (not pQ.empty()):
        #print("\nQ len", pQ.qsize())
        tempNode=pQ.get()
        tempNode = tempNode[2]
        if tempNode.index not in VisitedList:
            PathList.append(tempNode.index)
            VisitedList.append(tempNode.index)
            tempNode.PathfromStart.append(tempNode.index)
            
            if tempNode.isGoal :
                return (tempNode.PathfromStart)
            else:
                if (tempNode.index[0]+grid[tempNode.index] < arrsize ): #if x postion + cell value is less than max arrsize, valid       
                    indx = (tempNode.index[0]+grid[tempNode.index],tempNode.index[1])
                    downneighbor = Node(indx)
                    if (indx == goalCell):
                        downneighbor.isGoal = True
                    else:
                        downneighbor.isGoal = False
                    downneighbor.PathfromStart.extend(tempNode.PathfromStart)
                    downneighbor.mDis = getEuc(indx)
                    #print("Down Neighbor:",indx)
                    #print("Down Neighbor Path:",downneighbor.PathfromStart)
                    #print("Down Distance to goal:",downneighbor.mDis)
                    #print("\n")
                    cost = itercount + getEuc(downneighbor.index)
                    pQ.put((cost,count,downneighbor))
                    count+=1

                if (tempNode.index[0]-grid[tempNode.index] >= 0):
                    indx = (tempNode.index[0]-grid[tempNode.index],tempNode.index[1])
                    leftneighbor = Node(indx)
                    if (indx == goalCell):
                        leftneighbor.isGoal = True
                    else:
                        leftneighbor.isGoal = False
                    leftneighbor.PathfromStart.extend(tempNode.PathfromStart)
                    leftneighbor.mDis = getEuc(indx)
                    #print("Left Neighbor:",indx)
                    #print("Left Neighbor Path:",leftneighbor.PathfromStart)
                    #print("Left Distance to goal:",leftneighbor.mDis)
                    #print("\n")
                    cost = itercount + getEuc(leftneighbor.index)
                    pQ.put((cost,count,leftneighbor))
                    count+=1

                if (tempNode.index[1]-grid[tempNode.index] >= 0 ):
                    indx = (tempNode.index[0],tempNode.index[1]-grid[tempNode.index])
                    upneighbor = Node(indx)
                    if (indx == goalCell):
                        upneighbor.isGoal = True
                    else:
                        upneighbor.isGoal = False
                    upneighbor.PathfromStart.extend(tempNode.PathfromStart)
                    upneighbor.mDis = getEuc(indx)
                    #print("Up Neighbor:",indx)
                    #print("Up Neighbor Path:",upneighbor.PathfromStart)
                    #print("Up Distance to goal:",upneighbor.mDis)
                    #print("\n")
                    cost = itercount + getEuc(upneighbor.index)
                    pQ.put((cost,count,upneighbor))
                    count+=1
                    
                if (tempNode.index[1]+grid[tempNode.index] < arrsize ):
                    indx = (tempNode.index[0],tempNode.index[1]+grid[tempNode.index])
                    rightneighbor = Node(indx)
                    if (indx == goalCell):
                        rightneighbor.isGoal = True
                    else:
                        rightneighbor.isGoal = False
                    rightneighbor.PathfromStart.extend(tempNode.PathfromStart)
                    rightneighbor.mDis = getEuc(indx)
                    #print("Right Neighbor:",indx)
                    #print("Right Neighbor Path:",rightneighbor.PathfromStart)
                    #print("Right Distance to goal:",rightneighbor.mDis)
                    #print("\n")
                    cost = itercount + getEuc(rightneighbor.index)
                    pQ.put((cost,count,rightneighbor))
                    count+=1
        itercount+=1
    # JUST FOR COMPARISON
    #mymoves = BFS(arrsize,grid)
    #print(mymoves)

def drawAstar(path,grid):
    tmpmoves = numpy.full([arrsize, arrsize],-1,dtype = int)
    count = 0
    for i in range(len(path)):
        tmpmoves[path[i]] = count
        count+=1

    for i in range(len(path)):
        x = path[i][0]
        y = path[i][1]
        if (i+1<len(path)):
            tmpx = path[i+1][0]
            tmpy = path[i+1][1]
            if x == tmpx:
                distance = tmpy-y
                y+=1
                for y in range(distance):
                    if tmpmoves[x,y] ==-1 and distance>y:
                        tmpmoves[x,y]=-2
                    if tmpmoves[x,y] ==-1 and distance<y:
                        tmpmoves[x,y]=-2
                x= tmpx
            if y == tmpy:
                distance = tmpx-x
                x+=1
                for x in range(distance):
                    if tmpmoves[x,y] ==-1 and distance > x:
                        tmpmoves[x,y]=-2
                    if tmpmoves[x,y] ==-1 and distance < x:
                        tmpmoves[x,y]=-2
                y=tmpy
        #print(tmpmoves)
   

    Draw(arrsize,grid,tmpmoves,True)

#geneGrid= randGrid(arrsize)
def getAmoves(path):
    if path is None:
        return
    genemoves = numpy.full([arrsize, arrsize],-1,dtype = int)
    count = 0
    for i in range(len(path)):
        genemoves[path[i]] = count
        count+=1
    return genemoves



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Genetic Algorithm
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""




class chromoNode:
    def __init__(self,grid,moves):
        self.grid = grid
        self.moves = moves

def crossover(parent1,parent2):
    childgrid = numpy.full([arrsize, arrsize],-1,dtype = int)

    for row in range(arrsize):
        for col in range(arrsize):
            #print("Crossover...")
            whichparent = random.randint(1,2)
            if whichparent == 1: # crossover from child
                childgrid[row,col] = parent1.grid[row,col]
            if whichparent == 2: # crossover from parent 2
                childgrid[row,col] = parent2.grid[row,col]
    
    child = None
    if gaAstar == True:
        path = Astar(childgrid)
        if (path is None):
            crossover(parent1,parent2)
        childmoves = getAmoves(path)
        child = chromoNode(childgrid,childmoves)
    elif gaBfs == True:
        childmoves = BFS(arrsize,childgrid)
        if (childmoves[arrsize-1,arrsize-1]==-1):
            crossover(parent1,parent2)
        child = chromoNode(childgrid,childmoves)

    return child

def mutation(child):
    newChild = numpy.full([arrsize, arrsize],-1,dtype = int)
    newChild = child.grid

    for row in range(arrsize):
        for col in range(arrsize):
            x = random.randint(0,100)
            #print(x)
            if x < 10: # 10 percent chance of mutation
                #print("Mutating Cell...")
                num = random.randint(1,arrsize-1)
                while ((row+num>arrsize and row-num<0 and col+num>arrsize and col-num<0)):
                    num = random.randint(1,arrsize-1)
                newChild[row,col] = num
    
    newChildmoves = None
    if gaAstar == True:
        path = Astar(newChild)
        if (path is None):
            mutation(child)
        newChildmoves = getAmoves(path)
    elif gaBfs == True:
        newChildmoves = BFS(arrsize,newChild)
        if (newChildmoves[arrsize-1,arrsize-1]==-1):
            mutation(child)

    baby = chromoNode(newChild,newChildmoves)

    return baby

iterz=0
def add_one():
    global iterz
    iterz += 1

def makeBabies(children):
    add_one()

    first = None
    second = None
    #print("Making Babies Yay!")
    allchildren = children
    for i in range(len(allchildren)):
        if allchildren[i].moves is not None:
            if allchildren[i].moves[arrsize-1,arrsize-1] <= 2 and allchildren[i].moves[arrsize-1,arrsize-1] > 0:
                return allchildren[i]

    return None
    

def geneticAlgo(): # gets first two children
    #print("GENETIC ALGORITHM\n")

    puzzlez = []
    for i in range(10):
        x = randGrid(arrsize)
        path = Astar(x)
        y = None
        if gaAstar == True:
            while path is None:
                x = randGrid(arrsize)
                path = Astar(x)
            y = getAmoves(path)
        elif gaBfs == True:
            #print("here")
            y = BFS(arrsize,x)
            while (y[arrsize-1,arrsize-1]==-1):
                x = randGrid(arrsize)
                y = BFS(arrsize,x)
        chromo = chromoNode(x,y)
        puzzlez.append(chromo)

  
    parents = []
    
    first = None
    second = None
    for i in range (10):
        puzzle = puzzlez[i]
        if first is None:
            first = puzzle
        if first is not None:
            if puzzle.moves[arrsize-1,arrsize-1] <= first.moves[arrsize-1,arrsize-1]:
                second = first
                first = puzzle
    
    children = []
    for i in range(10):
        child = crossover(first,second)
        child = mutation(child)
        children.append(child)
    
    print("\nPLEASE WAIT\nCrossover & Mutation Happening......")
    best = makeBabies(children)
    while (best is None): 
        children = []
        for i in range(10):
            child = crossover(first,second)
            child = mutation(child)
            children.append(child)
        best = makeBabies(children)    
    return best


if runHill == True:
    print("\nHILL CLIMBING...\n")
    hillClimb(65)
elif runGA == True:
    print("\nGENETIC ALGORITHM...\n")
    checkA = gaAstar # draws for a star when Astar is true
    bestchild = geneticAlgo()
    print(bestchild.grid)
    print(bestchild.moves)
    moves = bestchild.moves
    print("Iterations: ",iterz)
    Draw(arrsize,bestchild.grid,moves,checkA)
elif runBFS == True:
    print("\nBFS SEARCH\n")
    grid = randGrid(arrsize)
    moves = BFS(arrsize,grid)
    Draw(arrsize,grid,moves,False)
elif runAstar == True:
    print("\nA* SEARCH\n")
    start = time.time()
    grid = randGrid(arrsize)
    path = Astar(grid)
    print("Path:",path)
    moves = getAmoves(path)
    Draw(arrsize,grid,moves,True) 
elif compare == True:
    print("\nBFS")
    start = time.time()
    grid = randGrid(arrsize)
    moves = BFS(arrsize,grid)
    print("BFS Time:",time.time() - start,"seconds")

    Draw(arrsize,grid,moves,False)

    print("\nASTAR")
    start = time.time()
    path = Astar(grid)
    amoves = getAmoves(path)
    print("Astar Time:",time.time() - start,"seconds")
    print("Path:",path)
    print("\n")
    Draw(arrsize,grid,amoves,True)



exit()
