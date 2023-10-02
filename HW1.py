print("Введите 3х-значное число")
num = int(input())

sumOfNum = 0

sumOfNum += num % 10
num //= 10
sumOfNum += num % 10
num //= 10
sumOfNum+= num
print (sumOfNum)