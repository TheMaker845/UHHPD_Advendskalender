import numpy as np
data=np.loadtxt("input.txt",delimiter=",",dtype="int")
print(sum(np.abs(data-np.median(data))))


fuel=[]
for best in range(min(data),max(data)):
    fuels=np.abs(data-best)
    fuels=fuels*(fuels+1)/2
    fuel.append(sum(fuels))
print("For position {0} the consumtion is {1}".format(np.argmin(fuel),min(np.array(fuel,dtype="int"))))
