import numpy as np
import matplotlib.pyplot as plt
import time

globaltime = time.time()
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
print(data)
mapdata=[]
fold=[]
for i in range(len(data)):
    if "fold along" not in data[i]:
        mapdata.append(data[i].split(","))
    else:
        fold.append(data[i][data[i].find("g")+2:].split("="))
mapdata=mapdata[:len(mapdata)-1]
mapdata=np.array(mapdata,dtype="int")
print(mapdata)


ysize=max(mapdata[:,1])+1
xsize=max(mapdata[:,0])+1
paper=np.zeros((ysize,xsize),dtype="int")
print(paper)
for place in mapdata:
    paper[place[1],place[0]]=1
print(paper)

def dofold(dir,pos):
    pos=int(pos)
    global paper
    global xsize
    global ysize
    if (dir=="y"):
        if (pos >= (ysize-1)/2):
            for y in range(pos+1,ysize):
                for x in range(xsize):
                    if paper[y,x]==1:
                        paper[y-2*(y-pos),x]=1
                        # print(y,y-2*(y-pos))
            paper=paper[:pos,:]
        if (pos < (ysize-1)/2):
            for y in range(0,pos):
                for x in range(xsize):
                    if paper[y,x]==1:
                        paper[y-2*(y-pos),x]=1
                        # print(y,y-2*(y-pos))
            paper=paper[pos:,:]
    if (dir=="x"):
        if (pos >= (xsize-1)/2):
            for x in range(pos+1,xsize):
                for y in range(ysize):
                    if paper[y,x]==1:
                        paper[y,x-2*(x-pos)]=1
                        # print(x,x-2*(x-pos))
            paper=paper[:,:pos]
        if (pos < (xsize-1)/2):
            for x in range(0,pos):
                for y in range(ysize):
                    if paper[y,x]==1:
                        paper[y,x-2*(x-pos)]=1
                        # print(x,x-2*(x-pos))
            paper=paper[:,pos:]
    xsize=len(paper[0])
    ysize=len(paper)




for folds in fold:
    plt.clf()
    dofold(*folds)
    print(paper)
    plt.imshow(paper, cmap='Reds', interpolation='nearest')
    plt.pause(0.5)


# dofold("x",5)

print("Visible Dots: {0}".format(np.sum(paper)))
# plt.savefig("Plot1.png",dpi=300)
# plt.savefig("Plot_V1.eps")
plt.show()
