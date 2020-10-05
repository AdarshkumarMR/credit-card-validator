from cs50 import get_string
n = get_string("credit card no: ")
number = []
for i in n:
    number.append(i)
length = len(number)
for i in range(0, length):
    number[i] = int(number[i])
temp = []
for i in range(length-2, -1, -2):
    temp.append(number[i]*2)
for i in range(0, len(temp)):
    if(temp[i] >= 10):
        temp[i] = int(temp[i]/10+temp[i]%10)
sum = 0
for i in temp:
    sum = sum+i
j = sum
grandsum = 0
for i in range(length-1,-1,-2):
    grandsum = grandsum+number[i]
key=grandsum+j
if(key % 10 == 0 and number[0] == 4):
    print("VISA\n")
elif(key % 10 == 0 and ((number[0] == 3 and number[1] == 4) or(number[0] == 3 and number[1] == 7))):
    print("AMEX\n")
elif(key % 10 == 0 and(number[0] == 5 and (number[1] == 1 or number[1] == 2 or number[1] == 3 or number[1] == 4 or number[1] == 5))):
    print("MASTERCARD\n")
else:
    print("INVALID\n")