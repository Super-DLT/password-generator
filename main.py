import random
#Basic Data
letters =["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numbers =["1","2","3","4","5","6","7","8","9","0"]
symbols = ["!","@","#","$","%","^","&","*","(",")"]
# Get user inputs
let = int(input("How many letters would you like in password?\n"))
num = int(input("How many numbers would you like in password?\n"))
sym = int(input("How many symbols would you like in password?\n"))
# Place Holder 
password = []
# Do some magic
for l in range (1, let + 1) :
    password.append(random.choice(letters))

for n in range (1, num + 1) :
    password.append(random.choice(numbers))

for s in range (1, sym + 1) :
    password.append(random.choice(symbols))
# Shuffle
result = random.shuffle(password)
#Place Holder 
result = ""
# Final result
for x in password :
    result += x
# Print
print(f"Your Password is : \n{result}")