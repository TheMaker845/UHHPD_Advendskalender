import numpy as np
import matplotlib.pyplot as plt


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
size=len(cave)


pos=np.zeros((size,size),dtype="int")
coord=[]
dist=[]


def ask(i,j,grid):
    if (-1<i<(len(grid))) and (-1<j<(len(grid[i]))):
        return cave[i][j]
    return -1
def pathfinder():
    size=len(cave)
    for x in range(size):
        for y in range(size):
            coord.append([x,y])
            dist.append(np.Infinity)
    dist[0]=0
    ccost=np.zeros((size,size))

    # print(dist)
    print("Estimated size:{0}".format(size**2))
    while len(coord)>0:
        u=np.argmin(dist)
        x=coord[u][0]
        y=coord[u][1]
        for cords in [[x-1,y],[x+1,y],[x,y+1],[x,y-1]]:
            x1=cords[0]
            y1=cords[1]
            A=ask(x1,y1,cave)
            if A!=-1 and [x1,y1] in coord:
                alt=dist[u]+cave[x1,y1]
                v=coord.index([x1,y1])
                if alt<dist[v]:
                    dist[v]=alt
                    ccost[x1,y1]=alt
        del coord[u]
        del dist[u]
    plt.imshow(ccost, cmap='hot', interpolation='nearest')
    print("Lowest Risk:{0}".format(int(ccost[size-1,size-1])))
print("Part 1")
pathfinder()
bigcave=[]
for i in range(5*size):
    line=[]
    for j in range(5*size):
        line.append(int(cave[i%size][j%size]+np.floor(j/size)+np.floor(i/size))%9)
    bigcave.append(line)
bigcave=np.array(bigcave)
bigcave[bigcave[:,:]==0]=9
print("Part 2")
cave=bigcave
# plt.imshow(ccost, cmap='Reds', interpolation='nearest')
plt.show()

# pathfinder()

# for i in range(5*size):
#     line=""
#     for j in range(5*size):
#         line+=str(bigcave[i,j])
#     print(line)
