# ________________________________Assigment no 3________________________
# ______1________
a = "Hey Bro! Whatssapp"
print(a)

# ____2__________
print("ALBERT EINSTEIN once said: ")
print('"A person who never made a mistake never tried anything new."')

# _______3_______
r = float(input("Enter radius: "))
print("area of circle of " + str(r) + " is: " + str(4 * 3.14 * r * r))

# ______4_________
num = int(input("enter a number: "))
if (num < 0):
    print("negative")
elif (num > 0):
    print("positive")
else:
    print("zero")

# ______5_________
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
check = input("enter any letter: ")
if check in vowels:
    print("Vowel")
else:
    print("consonants")

# _______6_________
h = int(input("enter hieght in cm: "))
w = int(input("enter weight in kg: "))
print("Bmi of given data is: " + str(10000 * w / (h * h)))

# _______7_________
names = ["huzaifa", "Sagheer", "Karrar", "Hadi"]
for i in range(len(names)): print(names[i])

# _______8__________
for i in range(len(names)): print("How are you! " + names[i] + " bro?")

# _______9___________
foods = ["Broast", "Zinger", "Beef burger", "pilao", "Biryani", "Karahi", "Tikka", "Bihari kabab", "Bihari boti"]
print("three items from beggining: " + str(foods[:2]))
print("three items from Middle: " + str(foods[2:5]))
print("three items from Last: " + str(foods[5:]))

# __________10___________________
foods = ["Broast", "Zinger", "Beef burger", "pilao"]
Frnds_food = ["Biryani", "Karahi", "Tikka", "Bihari kabab", "Bihari boti"]
foods.append("pizza")
Frnds_food.append("pizza fries")
print("My favourite dishes are: ")
for i in range(len(foods)):
    print(foods[i])
print("My frnds favourite dishes are: ")
for i in range(len(Frnds_food)):
    print(Frnds_food[i])
