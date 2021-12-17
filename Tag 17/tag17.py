import numpy as np
import matplotlib.pyplot as plt


# targetx=[20,30]
# targety=[-10,-5]

targetx=[153,199]
targety=[-114,-75]

def intarget(x,y):
    if targetx[0]<=x and x<=targetx[1] and targety[0]<=y and y<=targety[1]:
        return 0
    return 1
def shoot(vx,vy):
    pos=[]
    x=0
    y=0
    hit=1
    pos.append([0,0])
    for i in range(0,1000):
        if (vx-i*0>0):
            x+=vx-i*0
        y+=vy-i
        hit=hit*intarget(x,y)
        pos.append([x,y])
        if (hit==0 or y<targety[0] or x>targetx[1]):
            break
    return (np.array(pos),hit)
plt.axes()
rectangle = plt.Rectangle((targetx[0],targety[0]), targetx[1]-targetx[0], targety[1]-targety[0], fc='navy',ec="black",zorder=20)
plt.gca().add_patch(rectangle)
plt.xlim(0,200)
plt.ylim(-114,6500)


def findstop(deltax):
    return np.floor(np.sqrt(2*deltax))

# stopVx=findstop(targetx[0])
# maxvals=[]
# for vy in range(400-200):
#     r,hit=shoot(stopVx,vy)
#     if hit==0:
#         # plt.plot(r[:,0],r[:,1],".")
#         maxvals.append(max(r[:,1]))
# print("Max reched height at {0}".format(max(maxvals)))
maxvals=[]
for vx in range(1000):
    for vy in range(1000):
        r,hit=shoot(vx,vy-500)
        if hit==0:
            plt.plot(r[:,0],r[:,1],"-")
            maxvals.append(max(r[:,1]))

print("Max reched height at {0}".format(max(maxvals)))
print("number of starts {0}".format(len(maxvals)))
plt.show()
#
# with open ("test", "r") as myfile:
#     data=myfile.readlines()
# for i in range(len(data)):
#     data[i]=data[i][:len(data[i])-1].split(",")
# data=np.array(data,dtype="int")
# for i in starts:
#     print(len(starts))
#     if i in data:
#         print(i)
