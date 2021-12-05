import numpy as np

with open ("input.txt", "r") as myfile:
    data=myfile.readlines()


for i in range(len(data)):
     data[i]=data[i][:len(data[i])-1]


draw=np.array(data[0].split(","),dtype="int")
# print(draw)
Boards=[]
row=[]
for i in range(2,len(data)):
    if (data[i]==""):
        # print(np.array(row))
        Boards.append(np.array(row))
        row=[]
    elif (i==len(data)-1):
        row.append(np.array(data[i].split(),dtype="int"))
        # print(np.array(row))
        Boards.append(np.array(row))
        row=[]
    else:
        row.append(np.array(data[i].split(),dtype="int"))


bingo=False
bingboard=-1
bingnum=-1
nums=[22,8,21,6,1]
won=[]
for num in draw:
    for n_board in range(len(Boards)):
        for i in range(len(Boards[n_board])):
            for j in range(len(Boards[n_board][i])):
                if (Boards[n_board][i][j]==num):
                    Boards[n_board][i][j]=-1
    #CHECK

    for n_board in range(len(Boards)):
        bingo=False
        if not n_board in won:
            for i in range(len(Boards[n_board])):
                if (Boards[n_board][i][0]==-1) and (Boards[n_board][i][1]==-1) and (Boards[n_board][i][2]==-1) and (Boards[n_board][i][3]==-1) and (Boards[n_board][i][4]==-1):
                    # print("bingooooooooooooo")
                    bingo=True
                    break
            for i in range(len(Boards[n_board])):
                if (Boards[n_board][0][i]==-1) and (Boards[n_board][1][i]==-1) and (Boards[n_board][2][i]==-1) and (Boards[n_board][3][i]==-1) and (Boards[n_board][4][i]==-1):
                    # print("bingooooooooooooo")
                    bingo=True
                    break
            if bingo:
                bingboard=n_board
                bingnum=num
                won.append(n_board)
    if len(won)==len(Boards):
        break

winner=Boards[bingboard]
print(winner)
print(bingnum)
sum=0
for i in range(len(winner)):
    for j in range(len(winner[i])):
        if (winner[i][j]!=-1):
            sum+=winner[i][j]
print(sum*bingnum)
print(won)







# test="1, 2, 3, 4"
# print(np.array(test.split(","),dtype="int"))
