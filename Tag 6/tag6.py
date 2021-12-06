import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("input.txt",delimiter=",",dtype="int")
print(data)
data2=data[:]
# # data=np.append(data,82)
# for i in range(1,81):
#     for j in range(len(data)):
#         if (data[j]==0):
#             data=np.append(data,9)
#             data[j]=7
#     data=data-1
#     # print("After {0} days: {1} ".format(i,data))
# print(len(data))

fishis=np.zeros(9,dtype="double")
print(fishis)
for i in data2:
    fishis[i]+=1
print(fishis)
num=[]
for i in range(1000):
    fishis=np.roll(fishis,-1)
    fishis[6]+=fishis[8]
    num.append(sum(fishis))
    # print(fishis)
print(sum(fishis))
plt.plot(np.array(num))
plt.show()
