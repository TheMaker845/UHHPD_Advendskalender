import numpy as np
import matplotlib.pyplot as plt

with open ("input3.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
# print(data)
input=[]
output=[]
for i in range(len(data)):
    input.append(data[i].split("|")[0][:len(data[i].split("|")[0])-1].split(" "))
    output.append(data[i].split("|")[1][1:].split(" "))
# print(input)

inval=input[0]
a="0"
b="0"
c="0"
d="0"
e="0"
f="0"
g="0"
print(inval)
one=""
four=""
seven=""
eight=""
for code in inval:
    if (len(code)==2):
        one=code
    if (len(code)==4):
        four=code
    if (len(code)==3):
        seven=code
    if (len(code)==7):
        eight=code
print(one)
print(four)
print(seven)
print(eight)
#### Fix with one and seven
a = seven.replace(one[0], "").replace(one[1],"")
print(a)
##### VARY based on one
for i in range(2):
    if (i==0):
        c=one[0]
        f=one[1]
    if (i==1):
        c=one[1]
        f=one[0]
    ##### VARY based on four
    for j in range(2):
        if (i==0):
            b=four.replace(one[0], "").replace(one[1],"")[0]
            d=four.replace(one[0], "").replace(one[1],"")[1]
        if (i==1):
            b=four.replace(one[0], "").replace(one[1],"")[1]
            d=four.replace(one[0], "").replace(one[1],"")[0]
        print(a,b,c,d,e,f,g)
