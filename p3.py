sum = 0
while True:
  num = float(input("Enter an integer number: "))
  if num.is_integer() and num >= 0:
    num = int(num)
    break

for i in range(1, num+1):
  sum = sum + i

print("answer is:", sum)