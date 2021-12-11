import numpy as np
import matplotlib.pyplot as plt
import time
globaltime = time.time()
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
grid=[]
for i in range(len(data)):
    gridi=[]
    for j in range(len(data[i])):
        gridi.append(data[i][j])
    grid.append(gridi)
grid=np.array(grid,dtype="int")
print(grid)
def ask(i,j):
    if (-1<i<(len(grid))) and (-1<j<(len(grid[i]))):
        return grid[i][j]
    return -1
def inc(i,j):
    if (-1<i<(len(grid))) and (-1<j<(len(grid[i]))) and (grid[i][j] !=0):
        grid[i][j]+=1
flashes=0
def test(x1,x2,y1,y2,doinc=True):
    global flashes
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            if doinc:
                inc(x,y)
            if ask(x,y)>9:
                grid[x][y]=0
                flashes=flashes+1
                test(x-1,x+1,y-1,y+1)

plt.imshow(grid, cmap='Blues_r', interpolation='nearest',vmax=9)
allflashed=0
flash100=0
i=0
while True:
    plt.clf()
    grid+=1
    # print(flashes)
    test(0,10,0,10,False)
    plt.imshow(grid, cmap='Blues_r', interpolation='nearest',vmax=9)
    plt.title("step {0}".format(i+1))
    print(grid)
    plt.savefig("bilder/im_"+str(i)+".png",dpi=150)
    plt.pause(0.001)
    if (i+1==100):
        flash100=flashes
    if (np.max(grid)==0):
        allflashed=i+1
        break
    i+=1
print("Total flashes at {0} = {1}".format(100,flash100))
print("Total flashes {0}".format(flashes))
if (allflashed!=0):
    print("All flashed at {0}".format(allflashed))

plt.show()
