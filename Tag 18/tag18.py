import numpy as np
import matplotlib.pyplot as plt
# def split(word):
#     return [char for char in word]

def left(shrimpnumer,q):
    for i in range(q,-1,-1):
        if not shrimpnumer[i]  in "[,]":
            return i

    return -1

def right(shrimpnumer,q):
    for i in range(q,len(shrimpnumer),1):
        if not shrimpnumer[i]  in "[,]":
            return i
    return -1
def tostr(shrimpnumer):
    s=""
    for q in shrimpnumer:
        s+=str(q)
    return s

# shrimpnumer=list("[[6,[5,[4,[3,2]]]],1]")
# shrimpnumer=list("[[[[[9,8],1],2],3],4]")
# shrimpnumer="[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
# shrimpnumer="[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
# shrimpnumer[1]="15"
# shrimpnumer[3]="18"
def calcmagnitude(input):
    input=list(input)
    while len(input)>1:
        auf=-1
        zu=-1
        for i in range(len(input)):
            if "[" in input[i]:
                auf=i
            if "]" in input[i]:
                zu=i
            if (auf!=-1 and zu!=-1):
                break
        braket=input[auf+1:zu]
        res=3*int(braket[0])+2*int(braket[2])
        input[zu]=str(res)
        for i in range(auf,zu):
            del input[auf]
    return int(input[0])
def tolist(input):
    l=[]
    num=""
    for i in range(len(input)):
        if input[i] in "[,]":
            if num!="":
                l.append(num)
                num=""
            l.append(input[i])
        else: num+=input[i]
    return l


def reduce(shrimpnumer):
    shrimpnumer=list(shrimpnumer)
    opss=1
    while (opss!=0):
        ops=1
        while  (ops!=0):
            auf=-1
            deep=0
            zu=-1
            ops=0
            #print(tostr(shrimpnumer))
            for i in range(len(shrimpnumer)):
                if "[" in shrimpnumer[i]:
                    auf=i
                    deep+=1
                if "]" in shrimpnumer[i]:
                    zu=i
                    deep-=1
                if (auf!=-1 and zu!=-1 and deep>3 and auf<zu):
                    break
            if (deep>3):
                ops+=1
                X=int(shrimpnumer[auf+1])
                Y=int(shrimpnumer[zu-1])
                #print(tostr(shrimpnumer[auf:zu+1]))

                posl=left(shrimpnumer,auf)
                posr=right(shrimpnumer,zu)

                if (posl!=-1): shrimpnumer[posl]=str(int(shrimpnumer[posl])+X)
                if (posr!=-1): shrimpnumer[posr]=str(int(shrimpnumer[posr])+Y)
                shrimpnumer[zu]="0"
                for i in range(auf,zu):
                    del shrimpnumer[auf]
                # print("explode ",tostr(shrimpnumer))
                # print("")
        opss=0
        #print("try split",tostr(shrimpnumer))
        for i in range(len(shrimpnumer)):
            num=shrimpnumer[i]
            #print(num)
            if not str(num) in "[,]":
                num=int(num)
                if num>=10 and opss==0:
                    opss+=1
                    shrimpnumer[i]="["+str(int(np.floor(num/2.0)))+","+str(int(np.ceil(num/2.0)))+"]"
                    # print("split ",tostr(shrimpnumer))
                    # print("")
        #print(opss)
        shrimpnumer=tolist(tostr(shrimpnumer))
    return tostr(shrimpnumer)
def add(shrimpnumer1,shrimpnumer2):
    shrimpnumer=reduce("["+shrimpnumer1+","+shrimpnumer2+"]")
    return shrimpnumer

with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
#print(data)
sum=data[0]
for i in range(1,len(data)):
    # print(" ",sum)
    # print("+", data[i])
    sum=add(sum,data[i])
    # print("=",sum)
    # print("\n")
print(sum)
print("Final Magnitude {0}".format(calcmagnitude(sum)))
print("part 2")
magnitudes=[]
for i in range(len(data)):
    for j in range(len(data)):
        #if i!=j:
        magnitudes.append(calcmagnitude(add(data[i],data[j])))
print("Max magnitude {0}".format(max(magnitudes)))
#print(magnitudes)
plt.hist(magnitudes,bins=10)
plt.show()
#print(add("[[[[4,3],4],4],[7,[[8,4],9]]]","[1,1]"))
#print(tolist("[[[[4,3],4],4],[72,[[8,4],9]]]"))
#print(add("[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]","[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"))
