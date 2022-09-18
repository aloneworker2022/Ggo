import random
from funcs import *
from you import *
class WORD:
    def __init__(self):
        self.map = self.makemap()
        self.puttown(self.map)
        self.putmoster(self.map)


    def gameover(self):
        print("OVER")

    def puttown(self,maps):
        return self.putpoint(maps,10,20,1)

    def putpoint(self,maps,Min,Max,point):
        
        mount = random.randint(Min,Max)
        for _ in range(mount):
            x = random.randint(0,len(maps)-1)
            y = random.randint(0,len(maps[0])-1)
            maps[x][y] = point
        return maps

    
    def makemap(self):
        x = random.randint(20,100)
        y = random.randint(20,100)
        maps = [ [0 for i in range(x)] for k in range(y)]
        return maps


    def pointADD(self,maps,x,y,point):
        wher = random.randint(0,1)
        where = random.randint(-1,1)
        if wher == 1 :
            x += where 
            if x>= len(maps):
                x = 0 
            elif x < 0 :
                x = len(maps)-1
        elif wher == 0:
            y += where
            if y >= len(maps[x]):
                y = 0 
            elif y < 0 :
                y = len(maps[y])-1
        maps[x][y] = point

    def towngrown(self,maps):

        for x in range(len(maps)):
            mps = maps[x]
            for y in range(len(mps)):
                who = maps[x][y]
                if who == 1 :
                    wht = random.randint(0,4)
                    if wht == 1 :
                        self.pointADD(maps,x,y,1)
                    elif wht == 2 :
                        self.pointADD(maps,x,y,0)
        return maps

    def putmoster(self,maps):
        return self.putpoint(maps,10,20,2)
        maps = [str(i) for i in maps]
        print('\n'.join(map(''.join,maps)))

    def mosteraction(self,maps):
        for x in range(len(maps)):
            mps = maps[x]
            for y in range(len(mps)):
                who = maps[x][y]
                if who == 1 :
                    wht = random.randint(0,4)
                    if wht == 1 :
                        self.pointADD(maps,x,y,1)
                    elif wht == 2 :
                        self.pointADD(maps,x,y,0)
        return maps









