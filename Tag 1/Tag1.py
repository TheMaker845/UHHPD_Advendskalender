import numpy as np
import matplotlib.pyplot as plt

data=np.loadtxt("input.txt")
print(data)
counter=0
for i in range(1,len(data)):
    if (data[i]>data[i-1]): counter+=1
print(counter)

data2=[]
for i in range(2,len(data)):
    data2.append(data[i]+data[i-1]+data[i-2])
counter=0
for i in range(1,len(data2)):
    if (data2[i]>data2[i-1]): counter+=1
print(counter)

plt.plot(data,".")
plt.plot(np.array(data2)/3,".")
plt.show()
