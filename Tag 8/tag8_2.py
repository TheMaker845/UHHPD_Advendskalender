import numpy as np
import matplotlib.pyplot as plt
import time
globaltime = time.time()

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
# print(input)



def decomposeblock(inval,outval):
    a="0"
    b="0"
    c="0"
    d="0"
    e="0"
    f="0"
    g="0"

    def decode(code):
        if (a in code) and (b in code) and (c in code) and (e in code) and (f in code) and (g in code) and (len(code)==6):
            return 0
        if (c in code) and (f in code) and (len(code)==2):
            return 1
        if (a in code) and (c in code) and (d in code) and (e in code) and (g in code) and (len(code)==5):
            return 2
        if (a in code) and (c in code) and (d in code) and (f in code) and (g in code) and (len(code)==5):
            return 3
        if (b in code) and (c in code) and (d in code) and (f in code) and (len(code)==4):
            return 4
        if (a in code) and (b in code) and (d in code) and (f in code) and (g in code) and (len(code)==5):
            return 5
        if (a in code) and (b in code) and (d in code) and (e in code) and (f in code) and (g in code) and (len(code)==6):
            return 6
        if (a in code) and (c in code) and (f in code) and (len(code)==3):
            return 7
        if (a in code) and (b in code) and (c in code) and (d in code) and (e in code) and (f in code) and (g in code) and (len(code)==7):
            return 8
        if (a in code) and (b in code) and (c in code) and (d in code) and (f in code) and (g in code) and (len(code)==6):
            return 9
        return -1

    # print(inval)
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
    # print(one)
    # print(four)
    # print(seven)
    # print(eight)
    #### Fix with one and seven
    a = seven.replace(one[0], "").replace(one[1],"")
    # print(a)
    ##### VARY based on one
    search=False
    for i in range(2):
        if (i==0):
            c=one[0]
            f=one[1]
        if (i==1):
            c=one[1]
            f=one[0]
        ##### VARY based on four
        for j in range(2):
            if (j==0):
                b=four.replace(one[0], "").replace(one[1],"")[0]
                d=four.replace(one[0], "").replace(one[1],"")[1]
            if (j==1):
                b=four.replace(one[0], "").replace(one[1],"")[1]
                d=four.replace(one[0], "").replace(one[1],"")[0]
            for k in range(2):
                if (k==0):
                    e="abcdefg".replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(f, "")[0]
                    g="abcdefg".replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(f, "")[1]
                if (k==1):
                    e="abcdefg".replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(f, "")[1]
                    g="abcdefg".replace(a, "").replace(b, "").replace(c, "").replace(d, "").replace(f, "")[0]
                # print(a,b,c,d,e,f,g)
                found=0
                for code in inval:
                    num=decode(code)
                    if (num!=-1):
                        # print("{0} -> {1}".format(code,num))
                        found+=1
                if found==10:
                    # print("GOTCHAAAAAAAAAAAAAAAAAAAAAAAA")
                    search=True
                    break
                if search:
                    break
            if search:
                break
        if search:
            break
    resval=""
    for code in outval:
        num=decode(code)
        # print("{0} -> {1}".format(code,num))
        resval+=str(num)
    print("{0} {1} {2} {3} -> {4}".format(outval[0],outval[1],outval[2],outval[3],resval))
    return resval
# DO ALL CALCS:
sum=0
for (inp,outp) in zip(input,output):
    sum+=int(decomposeblock(inp,outp))
print("Sum over all = {0}".format(sum))
print('Runtime: {:2.2f}s'.format(time.time()-globaltime))
