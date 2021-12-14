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
maxgen=9
alphabeth="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def insert(string,gen=0,mid=False):
    stringlen=len(string)
    if (stringlen<3):
        newstr=""
        i=0
        while (i<len(string)):
            element=string[i:i+2]
            if (element in inserts[:,0]):
                ind=list(inserts[:,0]).index(element)
                newstr+=element[0]+inserts[ind,1]
            else:
                newstr+=element[0]
            i+=1
        if (gen < maxgen):
            print(newstr)
            return insert(newstr,gen+1)
        else:
            counts=[]
            if mid:
                newstr=newstr[1:len(newstr)-1]
            for i in alphabeth:
                a=newstr.count(i)
                counts.append(a)3
            return np.array(counts)

    else:
        stringA=string[:int(stringlen/2)]
        stringB=string.replace(stringA,"")
        stringC=stringA[len(stringA)-1]+stringB[0]
        return insert(stringA,gen,False)+insert(stringC,gen,True)+insert(stringB,gen,False)
    return 0
print(insert(string))
# print("points {0}".format(max(counts)-min(counts)))
