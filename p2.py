def loop():
  num = float(input("Enter an integer number: "))
  while num % 1 != 0:
    num = input("invalid input! Enter an integer number: ")

  if num % 2 == 0:
    print(num, "is even")
  elif num % 2 != 0:
    print(num, "is odd")

  loop_repeat = input("would you like to try another number?(Y / eny key): ")
  if loop_repeat == "Y" or loop_repeat == "y":
    loop()
  else:
    return

loop()

