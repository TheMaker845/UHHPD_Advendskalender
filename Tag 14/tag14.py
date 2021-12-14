import numpy as np
import time

globaltime = time.time()
with open ("input2.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
# print(data)
inserts=[]
string=data[0]

for i in range(2,len(data)):
    inserts.append(data[i].split(" -> "))
inserts=np.array(inserts)
# print(inserts)

def step(string):
    print("############")
    newstr=""
    i=0
    while (i<len(string)):
        element=string[i:i+2]
        if (element in inserts[:,0]):
            ind=list(inserts[:,0]).index(element)
            newstr+=element[0]+inserts[ind,1]
            print(inserts[ind,1])
        else:
            newstr+=element[0]
        i+=1
    return newstr
for q in range(3):
    string=step(string)
    print("Step {0}: {1}".format(q+1,string))

alphabeth="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
counts=[]
for i in alphabeth:
    a=string.count(i)
    if not (a==0):
        counts.append(a)
print("points {0}".format(max(counts)-min(counts)))
