num = input("please input a decimal number: ")
integerPart = num \ 1
decimalPart = num % 1

sum = integerPart * 10 + decimalPart * 100
print("output is:",sum)
