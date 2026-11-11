count = 0

text = input("Enter some text: ")
for i in range(len(text)):
  x = text[i]
  if x == 'a' or x == 'A' or x == 'i' or x == 'I' or x == 'o' or x == 'O' or x == 'u' or x == 'U' or x == 'e' or x == 'E':
    count = count + 1

print(count , "vowel")