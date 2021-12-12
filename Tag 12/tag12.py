import numpy as np
import matplotlib.pyplot as plt
import time

globaltime = time.time()
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
# print(data)
map=[]
for i in range(len(data)):
    map.append(np.array(data[i].split("-")))
    map.append(np.roll(np.array(data[i].split("-")),1))
map=np.array(map)
lowercase=[]
for i in range(len(map)):
    if (any(c for c in map[i][0] if c.islower())) and (not map[i][0] in lowercase) and (map[i][0]!="start") and (map[i][0]!="end"):
        lowercase.append(map[i][0])
paths=[]
youOnlyLiveTwice=""
def countel(inlist,item):
    c=0
    for elem in inlist:
        if (item==elem):
            c+=1
    return c
def pathfinder(path):
    global youOnlyLiveTwice
    last=path[len(path)-1]
    if (last=="end"):
        if (list(path) not in paths): #and (countel(path,youOnlyLiveTwice)<=2):
            paths.append(list(path))
    else:
        for conection in map:
            if last==conection[0]:
                next=conection[1]
                if any(c for c in next if c.islower()) and (next != youOnlyLiveTwice):
                    if not (next in path):
                        pathfinder(np.append(path,next))
                elif (countel(path,youOnlyLiveTwice)<2) and (next == youOnlyLiveTwice):
                    pathfinder(np.append(path,next))
                elif (next != youOnlyLiveTwice):
                    pathfinder(np.append(path,next))
for lower in lowercase:
    #youOnlyLiveTwice=lower ## exclude for Part 1
    print(lower)
    pathfinder(["start"])
for path in paths:
    print(path)
print("total number of paths: {0}".format(len(paths)))
print('Runtime: {:2.2f}s'.format(time.time()-globaltime))

# Coords={}
# for i in range(len(map)):
#     if  (not map[i][0] in Coords):
#         Coords[map[i][0]]=[np.random.random()*10,np.random.random()*10]
# print(Coords)
# for key in Coords.keys():
#     plt.scatter(Coords[key][0],Coords[key][1])
# for path in paths:
#     for i in range(1,len(path)):
#         plt.plot([Coords[path[i]][0],Coords[path[i-1]][0]],[Coords[path[i]][1],Coords[path[i-1]][1]])
# plt.show()
