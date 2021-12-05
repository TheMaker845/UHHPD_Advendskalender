import numpy as np
import matplotlib.pyplot as plt

with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
     data[i]=data[i][:len(data[i])-1]
start=[]
end=[]
for i in range(len(data)):
    start.append(data[i].split("->")[0].split(","))
    end.append(data[i].split("->")[1].split(","))
start=np.array(start,dtype="int")
end=np.array(end,dtype="int")
# print(start,end)
maxpos=np.max([np.max(start),np.max(end)])
grid=np.zeros((maxpos+1,maxpos+1),dtype="int")
def count(grid):
    counter=0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[j,i]>1):
                counter+=1
    return counter
def printter(grid):
    for i in range(len(grid)):
        stringi=""
        for j in range(len(grid[i])):
            if (grid[j,i]==0):
                stringi+="."
            else:
                stringi+=str(np.round(grid[j,i],0))
        print(stringi)
def plotline(i,j):
    if (i[0]==j[0]):
        for q in range(i[1],j[1]+1):
            grid[i[0],q]=grid[i[0],q]+1
        for q in range(j[1],i[1]+1):
            grid[i[0],q]=grid[i[0],q]+1
    if (i[1])==[j[1]]:
        for q in range(i[0],j[0]+1):
            grid[q,i[1]]=grid[q,i[1]]+1
        for q in range(j[0],i[0]+1):
            grid[q,i[1]]=grid[q,i[1]]+1
    if (i[0]<j[0]) and (i[1]<j[1]):
        for q in range(j[0]+1-i[0]):
            grid[i[0]+q,i[1]+q]+=1
            # print(i[0]+q,i[1]+q)
        print(i,j)
    if (i[0]>j[0]) and (i[1]>j[1]):
        for q in range(i[0]+1-j[0]):
            grid[j[0]+q,j[1]+q]+=1
            # print(j[0]+q,j[1]+q)
        print(i,j)
    if (i[0]<j[0]) and (i[1]>j[1]):
        for q in range(j[0]+1-i[0]):
            grid[i[0]+q,i[1]-q]+=1
            # print(i[0]+q,i[1]-q)
        print(i,j)
    if (i[0]>j[0]) and (i[1]<j[1]):
        for q in range(i[0]+1-j[0]):
            grid[i[0]-q,i[1]+q]+=1
            # print(i[0]-q,i[1]+q)
        print(i,j)

    # printter(grid)

for (i,j) in zip(start,end):
    plotline(i,j)

# printter(grid)
print("There are {0} overlaps".format(count(grid)))

plt.imshow(grid, cmap='hot', interpolation='nearest')
plt.savefig("Plot.png",dpi=300)
plt.savefig("Plot_V.eps")
plt.show()
