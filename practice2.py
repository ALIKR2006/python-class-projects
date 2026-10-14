num = float(input("Please input a decimal number: "))

if num >= 0:
    integerPart = num // 1
else:
    integerPart = num // 1 + 1

decimalPart = num - integerPart

result = integerPart * 10 + decimalPart * 100

print("Output is:", result)
