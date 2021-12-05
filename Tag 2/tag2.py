import numpy as np
import matplotlib.pyplot as plt
num=[]
dir=[]

with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    dir.append(data[i][:len(data[i])-3])
    num.append(data[i][len(data[i])-2:len(data[i])-1])
num=np.array(num,dtype="int")

hoz=0
depth=0
for (com,val) in zip(dir,num):
    if (com=="forward"):
        hoz+=val
    if (com=="down"):
        depth+=val
    if (com=="up"):
        depth-=val
print(hoz,depth)
print(hoz*depth)


print("PART 2")
hoz=0
depth=0
aim=0
for (com,val) in zip(dir,num):
    if (com=="forward"):
        hoz+=val
        depth+=aim*val
    if (com=="down"):
        aim+=val
    if (com=="up"):
        aim-=val
print(hoz,depth)
print(hoz*depth)
