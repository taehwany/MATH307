import csv 
with open('Lottery_Mega_Millions.csv') as f:
    reader = csv.reader(f)
    next(reader)
    newData = []
    data = []
    x = 0
    count1 = 0
    count2 = 0
    count3 = 0
    instance = 0
    for row in reader:
        i = row[1]
        temp_list = i.split(' ')
        temp = []
        for num in temp_list:
            temp.append(int(num))
            x = x + 1
        newData.append(temp)
        for num1 in newData:
            count1 = 0
            count2 = 0
            count3 = 0
            for num2 in num1:
                if num2 < 20:
                    count1 = count1 + 1
                if 41 > num2 > 19:
                    count2 = count2 + 1
                if num2 > 40:
                    count3 = count3 + 1
        if count1 == 2:
            if count2 == 2:
                if count3 == 1:
                    instance = instance + 1
#instances that happened
print (instance)
historicalProbability = instance/x
print (historicalProbability)
