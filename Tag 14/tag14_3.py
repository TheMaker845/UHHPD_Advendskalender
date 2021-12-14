import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit as cf
import time

globaltime = time.time()
with open ("input.txt", "r") as myfile:
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
alphabeth="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
stack=np.zeros(len(inserts))
bstack=np.zeros(26)
# print(stack)
# print(inserts[:,0])
for i in range(0,len(string)-1):
    element=string[i:i+2]
    # print(element)
    ind=list(inserts[:,0]).index(element)
    stack[ind]+=1
for i in string:
    bstack[alphabeth.find(i)]+=1

values=[]
for q in range(20):
    Rstack=np.zeros(len(inserts))
    for i in range(len(stack)):
        ins=inserts[i,1]
        # if stack[i]!=0:
        #     print(ins,stack[i])
        bstack[alphabeth.find(ins)]+=stack[i]
        el1=inserts[i,0][0]+ins
        el2=ins+inserts[i,0][1]
        # ind=list(inserts[:,0]).index(el1)
        Rstack[inserts[:,0]==el1]+=stack[i]
        # ind=list(inserts[:,0]).index(el2)
        Rstack[inserts[:,0]==el2]+=stack[i]
    stack=Rstack
    res=[]
    for b in bstack:
        if not b==0:
            res.append(b)
    val=(max(res)-min(res))
    values.append(val)






res=[]
for b in bstack:
    if not b==0:
        res.append(b)
print(max(res)-min(res))
print('Runtime: {:2.3f}s'.format(time.time()-globaltime))

def func(x,A,B,D,C):
    return A*np.exp(B*x+D)+C*x**3
y=np.array(values)
maxx=max(y)
y=y/max(y)
plt.plot(y,".")
par,covM=cf(func,np.arange(20),y,bounds=([0,0,-10,-10],[6,1,10,3]))
print(par)
print(covM)
x=np.linspace(0,40,1000)
plt.plot(x,func(x,*par))
print(func(40,*par)*maxx/3776553567525.0)
# plt.plot(x,func(x,9,0.8,2))
plt.yscale("log")

plt.show()
