import numpy as np
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]

gamma=""
epsilon=""

for i in range(len(data[0])):
    one=0
    zero=0
    for j in range(len(data)):
        if (data[j][i]=="1"):
            one+=1
        if (data[j][i]=="0"):
            zero+=1
    if (one>zero):
        gamma=gamma+"1"
        epsilon=epsilon+"0"
    if (one<zero):
        gamma=gamma+"0"
        epsilon=epsilon+"1"
    if (one==zero):
        print("HÄÄÄÄ")
print(gamma,epsilon)

def bintodec(gamma):
    num=0
    for i in range(len(gamma)):
        num+=int(gamma[len(gamma)-i-1])*2**(i)
        # print(gamma[i])
    return num

print(bintodec(gamma),bintodec(epsilon))
print(bintodec(gamma)*bintodec(epsilon))


def findmax(data):
    gamma=""
    epsilon=""

    for i in range(len(data[0])):
        one=0
        zero=0
        for j in range(len(data)):
            if (data[j][i]=="1"):
                one+=1
            if (data[j][i]=="0"):
                zero+=1
        if (one>=zero):
            gamma=gamma+"1"
            epsilon=epsilon+"0"
        if (one<zero):
            gamma=gamma+"0"
            epsilon=epsilon+"1"
        # if (one==zero):
            # print("HÄÄÄÄ")
    return(gamma,epsilon)


def ex2(indata,num=0):
    j=0
    while (len(indata)>1):
        A,B=findmax(indata)
        if (num==1):
            A=B
        rem=[]
        for i in range(len(indata)):
            if (A[j]!=indata[i][j]):
                rem.append(indata[i])
        for i in range(len(rem)):
            indata.remove(rem[i])
        j=j+1
        if (j>=len(indata[0])):
            j=0
            print("reset")
        print(len(indata))
    return(indata[0])

A=ex2(data[:])
print(A)
B=ex2(data[:],1)
print(B)

print(bintodec(A),bintodec(B))
print(bintodec(A)*bintodec(B))
