import numpy as np


with open ("input2.txt", "r") as myfile:
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

ccost=np.zeros((size,size))+np.Infinity
ccost[0,0]=0
pos=np.zeros((size,size),dtype="int")

def ask(i,j,grid):
    if (-1<i<(len(grid))) and (-1<j<(len(grid[i]))):
        return cave[i][j]
    return -1
# pos[0,0]=1
print(ccost)
print(pos)

def step(x,y,steps):
    global ccost
    global pos
    if steps<40:
        print(steps)
        print(x,y)
        print(pos)
        print(ccost)
        pos[x,y]=1
        if np.sum(pos)<(size**2):
            cur=ccost[x,y]
            mincost=np.Infinity
            newcords=[0,0]
            for cords in [[x-1,y],[x+1,y],[x,y+1],[x,y-1]]:
                x1=cords[0]
                y1=cords[1]
                A=ask(x1,y1,cave)
                if A!=-1 and pos[x1,y1]!=1:
                    cost=cur+A
                    if (cost<=ccost[x1,y1]):
                        ccost[x1,y1]=cost
                    if (ccost[x1,y1]<mincost):
                        mincost=ccost[x1,y1]
                        newcords=[x1,y1]
            step(newcords[0],newcords[1],steps+1)
step(0,0,0)
# print(ccost)
print(pos)
# import numpy as np
#
#
# maze = np.genfromtxt("input2.txt", delimiter=1, dtype=np.uint16)
#
# rows, cols = maze.shape
#
# maze_sum = np.zeros_like(maze)
# maze_sum[0, :] += np.cumsum(maze[0, :])
# maze_sum[:, 0] += np.cumsum(maze[:, 0])
# maze_sum[0, 0] -= 1
#
#
# for row in range(1, rows):
#     for col in range(1, cols):
#         maze_sum[row, col] = min(maze_sum[row - 1, col] + maze[row, col],
#                                  maze_sum[row, col - 1] + maze[row, col])
# print(maze_sum)
# print(maze_sum[rows - 1, cols - 1] - maze[0, 0])
