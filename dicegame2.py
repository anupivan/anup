#dicegame
import random
while True:
	i=input("enter r to roll or q to quit")
	if(i=='r'):
		print(random.randint(1,6))
	else:
		print("bye!")
		exit()
	
		