import numpy as np
import matplotlib.pyplot as plt

import time

globaltime = time.time()
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
# print(data)
cave=[]
for dat in data:
    row=[]
    for i in dat:
        row.append(i)
    cave.append(row)
cave=np.array(cave,dtype="int")
print(cave)
size=len(cave)

maxpathval=sum(cave[0,:])+sum(cave[:,size-1])-cave[0,0]-cave[0,size-1]
print(maxpathval)
# maxpathval=710
def ask(i,j):
    if (-1<i<(len(cave))) and (-1<j<(len(cave[i]))):
        return cave[i][j]
    return -1


def pathfinder(path,coord):
        global maxpathval
        path=np.append(path,ask(coord[0],coord[1]))
        if (sum(path)<maxpathval):
            if ((coord[0]==size-1) and (coord[1]==size-1)):
                maxpathval=sum(path)
                print(coord,sum(path))
            else:
                if (ask(coord[0]+1,coord[1])!=-1):
                    pathfinder(path,[coord[0]+1,coord[1]])
                if (ask(coord[0],coord[1]+1)!=-1):
                    pathfinder(path,[coord[0],coord[1]+1])
                # if (ask(coord[0]-1,coord[1])!=-1):
                #     pathfinder(path,[coord[0]-1,coord[1]])
                # if (ask(coord[0],coord[1]-1)!=-1):
                #     pathfinder(path,[coord[0],coord[1]-1])
pathfinder(np.array([-cave[0,0]]),[0,0])
print(maxpathval)
