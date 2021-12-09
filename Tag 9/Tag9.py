import numpy as np
import matplotlib.pyplot as plt
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
    return 20
dangerzone=0
min=[]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (ask(i,j)<ask(i+1,j)) and (ask(i,j)<ask(i-1,j)) and (ask(i,j)<ask(i,j+1)) and (ask(i,j)<ask(i,j-1)):
            dangerzone+=1+grid[i][j]
            min.append([i,j])

print(dangerzone)
used=[]
print(min)
i=2
j=2
def next(i,j):
    res=0
    used.append([i,j])
    if (9>ask(i+1,j)>ask(i,j)) and not [i+1,j] in used:
        res+= 1+next(i+1,j)
    if (9>ask(i-1,j)>ask(i,j)) and not [i-1,j] in used:
        res+= 1+next(i-1,j)
    if (9>ask(i,j+1)>ask(i,j)) and not [i,j+1] in used:
        res+= 1+next(i,j+1)
    if (9>ask(i,j-1)>ask(i,j)) and not [i,j-1] in used:
        res+= 1+next(i,j-1)
    return res
maxval=np.zeros(3)
uses=[0,0,0]
for i in min:
    used=[]
    clusterValue=next(i[0],i[1])+1
    print(clusterValue)
    if (clusterValue>np.min(maxval)):
        maxval[np.argmin(maxval)]=clusterValue
        uses[np.argmin(maxval)]=used

print(maxval)
print(uses)
prod=1
plt.imshow(grid, cmap='Reds', interpolation='nearest')
plt.savefig("Plot1.png",dpi=300)
plt.savefig("Plot_V1.eps")
plt.show()
for i in range(len(maxval)):
    prod*=maxval[i]
    for j in uses[i]:
        grid[j[0]][j[1]]=0

print(prod)

plt.imshow(grid, cmap='Reds', interpolation='nearest')
plt.savefig("Plot.png",dpi=300)
plt.savefig("Plot_V.eps")
plt.show()
