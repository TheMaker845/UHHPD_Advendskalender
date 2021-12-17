import numpy as np
import time
globaltime = time.time()
with open ("input.txt", "r") as myfile:
    data=myfile.readlines()
for i in range(len(data)):
    data[i]=data[i][:len(data[i])-1]
input=data[0]
# print(input)

def binToDec(gamma):
    num=0
    for i in range(len(gamma)):
        num+=float(gamma[len(gamma)-i-1])*2**(i)
        # print(gamma[i])
    return num
def HexToBin(inv):
    if inv=="0": return "0000"
    if inv=="1": return "0001"
    if inv=="2": return "0010"
    if inv=="3": return "0011"
    if inv=="4": return "0100"
    if inv=="5": return "0101"
    if inv=="6": return "0110"
    if inv=="7": return "0111"
    if inv=="8": return "1000"
    if inv=="9": return "1001"
    if inv=="A": return "1010"
    if inv=="B": return "1011"
    if inv=="C": return "1100"
    if inv=="D": return "1101"
    if inv=="E": return "1110"
    if inv=="F": return "1111"

    return 0
bin=""

# input="8A004A801A8002F478"
#input="620080001611562C8802118E34"
#input="D2FE28"
# input="C0015000016115A2E0802F182340"
# input="A0016C880162017C3686B18A3D4780"
# input="880086C3E88112"
#input="C200B40A82"
#input="9C0141080250320F1802104A08"
#input="9C005AC2F8F0"
#input="CE00C43D881120"
# input="880086C3E88112"

allvals=[]
secondtry=[]
for inv in input:
    bin+=HexToBin(inv)
versions=[]
def returns(op,lit):
    if (op==0):
        return(np.sum(lit))
    if (op==1):
        return(np.prod(lit))
    if (op==2):
        return(np.min(lit))
    if (op==3):
        return(np.max(lit))
    if (op==5):
        if (lit[0]>lit[1]):
            return 1
        return 0
    if (op==6):
        if (lit[0]<lit[1]):
            return 1
        return 0
    if (op==7):
        if (lit[0]==lit[1]):
            return 1
        return 0
def decode(bin):
    # print(bin)
    V=int(binToDec(bin[:3]))
    versions.append(V)
    T=int(binToDec(bin[3:6]))
    R=bin[6:]
    # print("version {0}".format(V))
    # print("type ID {0}".format(T))
    if (T==4):
        lit=[]
        move=0
        while True:
            val=R[0]
            # print(R[1:5])
            lit.append(R[1:5])
            R=R[5:]
            if (val=="0"):
                break
        result=""
        for i in lit:
            result+=i
        result=binToDec(result)
        secondtry.append(str(result))
        allvals.append(result)
        # print(result)
        return (R,result)
    if (T != 4):
        secondtry.append("(")
        secondtry.append("OP"+str(T))
        I=int(R[:1])
        R=R[1:]
        # print("lengh type ID {0}".format(I))
        lit=[]
        if (I==1):
            L=int(binToDec(R[:11]))
            R=R[11:]
            # print("number of sub-packets {0}".format(L))
            for i in range(L):
                # print("Run "+str(i))
                R,tLit=decode(R)
                lit.append(tLit)
            # return (R,returns(T,lit))
        if (I==0):
            L=int(binToDec(R[:15]))
            R=R[15:]
            # print("Len of sub-packets {0}".format(L))
            Q=R[:L]
            R=R[L:]
            while len(Q)>0:
                Q,tLit=decode(Q)
                lit.append(tLit)
        secondtry.append(")")
        return (R,returns(T,lit))
R,val=decode(bin)
print("Version sum {0}".format(sum(versions)))
print("Resulting Value {0}".format(val))

print('Runtime: {:2.3f}s'.format(time.time()-globaltime))

# print("Resulting Value {0}".format(258888628940))
# print(sum(allvals))
# print(2219384044554 )
# print(secondtry)
#
# while len(secondtry)>1:
#     auf=-1
#     zu=-1
#     for i in range(len(secondtry)):
#         if "(" in secondtry[i]:
#             auf=i
#         if ")" in secondtry[i]:
#             zu=i
#         if (auf!=-1 and zu!=-1):
#             break
#     braket=secondtry[auf+1:zu]
#     # print(braket)
#     op=int(braket[0][2])
#     vals=np.array(braket[1:],dtype="float")
#     # print(op)
#     # print(vals)
#     res=returns(op,vals)
#     # print(res)
#     secondtry[zu]=str(res)
#     # print(auf,zu)
#
#     for i in range(auf,zu):
#         # print(i)
#         del secondtry[auf]
# secondtry=np.array(secondtry,dtype="float")
# print("Resulting Value carry me UWU {0}".format(secondtry[0]))
#"258888628940"
