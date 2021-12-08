import numpy as np
import matplotlib.pyplot as plt

with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
# print(data)
input=[]
output=[]
for i in range(len(data)):
    input.append(data[i].split("|")[0][:len(data[i].split("|")[0])-1].split(" "))
    output.append(data[i].split("|")[1][1:].split(" "))
print(output)
eazy=0
for i in range(len(output)):
    for code in output[i]:
        if (len(code)==2):
            eazy+=1
        if (len(code)==4):
            eazy+=1
        if (len(code)==3):
            eazy+=1
        if (len(code)==7):
            eazy+=1
print(eazy)
