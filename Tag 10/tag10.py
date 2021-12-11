import numpy as np
import matplotlib.pyplot as plt
import time
globaltime = time.time()
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
# print(data)
allowedOpen="([{<"
allowedclosed=")]}>"

def check(line, completeness=False):
    syntax=[]
    syntax.append(line[0])
    def op(char):
        return allowedclosed[allowedOpen.find(char)]
    for i in range(1,len(line)):
        # print(syntax)
        if len(syntax)>0:
            if (line[i]) == op(syntax[-1]):
                     syntax.pop()
            elif (line[i] in allowedOpen):
                 syntax.append(line[i])
            else:
                # print("-{0}- Expected {1} , but found {2} instead".format(line,op(syntax[-1]),line[i]))
                return line[i]
                break
        else:
            syntax.append(line[i])
    if completeness:
        comp=""
        for i in range(len(syntax)):
            comp+=op(syntax[len(syntax)-1-i])
        # print("-{0}- Complete by adding {1}.".format(line,comp))
        return comp
    return "0"
# check("[(()[<>])]({[<{<<[]>>(")
# "[(()[<>])]({[<{<<[]>>("
# # line="[(()[<>])]({[<{<<[]>>("
def calcpoints(char):
    if char==")":
        return 3
    if char=="]":
        return 57
    if char=="}":
        return 1197
    if char==">":
        return 25137
    return 0
points=0
incomp=[]
for line in data:
    char=check(line)
    if (char=="0"):
        incomp.append(line)
    points+=calcpoints(char)
print("Tolal Points: {0}".format(points))
# print(incomp)
def calcpoints2(char):
    point=0
    for i in char:
        point*=5
        point+=allowedclosed.find(i)+1
    return point
score=[]
for line in incomp:
    score.append(calcpoints2(check(line,True)))
# print(score)
print("Tolal score: {0}".format(np.median(np.array(score))))
print('Runtime: {:2.3f}s'.format(time.time()-globaltime))
