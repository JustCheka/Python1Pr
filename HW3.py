print("Введите номер билета (6 знаков)")
num = input()
num1 = int(num[:3])
num2 = int(num[3:])

sumOfNum1 = 0
sumOfNum1 += num1 % 10
num1 //= 10
sumOfNum1 += num1 % 10
num1 //= 10
sumOfNum1 += num1

sumOfNum2 = 0
sumOfNum2 += num2 % 10
num2 //= 10
sumOfNum2 += num2 % 10
num2 //= 10
sumOfNum2 += num2

if (sumOfNum1 == sumOfNum2):
     print("Yes")
else:
     print("No")