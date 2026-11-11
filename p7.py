upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
output_text = ""


text = input("Enter some dummy text: ")
for char in text:
  for j in range(26):
    if char == lower[j]:
      char = upper[j]
      break
  output_text += char
   
print(output_text)