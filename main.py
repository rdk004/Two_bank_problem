from random import randint
count_array = []
bank_temp_array = []
for i in range(1,1000):
    bank_0 = [0,0,0,0]
    bank_temp = [bank_0]
    length = len(bank_temp)
    count = 0
    while bank_temp[length-1]!= [1,1,1,1] :
        if count%2 == 0:
            if count == 0:
                bank_temp.append([1,0,1,0])
                length = len(bank_temp)
                count+=1
            else :
                bank_temp.append([1,randint(0,1),randint(0,1),randint(0,1)])
                if ((bank_temp[count+1][1] != bank_temp[count][1] and bank_temp[count+1][2] != bank_temp[count][2]) or (bank_temp[count+1][2] != bank_temp[count][2] and bank_temp[count+1][3] != bank_temp[count][3]) or (bank_temp[count+1][3] != bank_temp[count][3] and bank_temp[count+1][1] != bank_temp[count][1])):
                    del bank_temp[-1]
                    length = len(bank_temp)
                else :
                    if bank_temp[count + 1] == [1, 0, 0, 0] or bank_temp[count + 1] == [1, 1, 0, 0] or bank_temp[count + 1] == [1, 0, 0, 1]:
                        del bank_temp[-1]
                        length = len(bank_temp)
                    else :
                        count+=1
                        length = len(bank_temp)
        else :
            bank_temp.append([0, randint(0, 1), randint(0, 1), randint(0, 1)])
            if ((bank_temp[count+1][1] != bank_temp[count][1] and bank_temp[count+1][2] != bank_temp[count][2]) or (bank_temp[count+1][2] != bank_temp[count][2] and bank_temp[count+1][3] != bank_temp[count][3]) or (bank_temp[count+1][3] != bank_temp[count][3] and bank_temp[count+1][1] != bank_temp[count][1])):
                del bank_temp[-1]
                length = len(bank_temp)
            else :
                if bank_temp[count + 1] == [0, 1, 1, 0] or bank_temp[count + 1] == [0, 0, 1, 1] or bank_temp[count+1] == [0,1,1,1]:
                    del bank_temp[-1]
                    length = len(bank_temp)
                else :
                    count+=1
                    length = len(bank_temp)
    count_array.append(count)
    bank_temp_array.append(bank_temp)
min_index = count_array.index(min(count_array))
count = count_array[min_index]
bank_temp = bank_temp_array[min_index]
print("The step description is as follows: ",bank_temp)
print("The minimum number of steps required for the man is: ",count+1)





