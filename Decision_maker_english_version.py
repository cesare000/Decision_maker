"""TO MY FUTURE EMPLOYER WHO IS VISITING MY GITHUB :) 
   As you know I'm italian and this whole program is written 
   in italian, I'm only 15 so it is probably bad written but it
   is a very basic program, I'll explain it in the following lines:
   have you ever been unncertain on what to choose? Well, in this 
   program you can insert the number of things in which you wanna
   choose, then you write them and this mini-software will choose for 
   you. Have a good day and employ me please ;)."""



import random

LIST = []
question = int(input("How many things are you not uncertain on? "))

max_length = question

while len(LIST) < max_length:
	item = input("Insert the item: ")
	LIST.append(item)

decision = random.choice(LIST)
final_decision = f"I've chosen {decision}." 
print(final_decision)

