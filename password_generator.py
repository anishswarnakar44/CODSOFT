import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!', '#', '$', '%', '&', '(', ')', '*', '+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
print("Welcome to the PyPassword Generator!")
let = int(input("How many letters would you like in your password?\n"))
pass_list = []

for i in range(1, let + 1):
  pass_list.append(random.choice(letters))

passw= ""
for i in pass_list:
  passw += i

print(f"Your password is: {passw}")
