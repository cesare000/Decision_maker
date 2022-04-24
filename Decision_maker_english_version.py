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

