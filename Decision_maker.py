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
domanda = int(input("Su quante cose sei indeciso/a? "))

lunghezza_massima = domanda

while len(LIST) < lunghezza_massima:
	item = input("Inserisci la cosa su cui sei inteciso: ")
	LIST.append(item)

scelta = random.choice(LIST)
decisione_finale = f"Ho scelto {scelta}." 
print(decisione_finale)

