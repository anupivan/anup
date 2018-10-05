#rockpappersissor
import random
d={1:'r',2:'p',3:'s'}
C=d[random.randint(1,3)]
while(1):
	U=input("enter 'r',p','s'")
	if(C=='r' and U=='s' or C=='p' and U=='r' or C=='s' and U=='p'):		
		print(C,"computer wins")
	elif(C==U):
		print(C,"tie")
	else:
		print(U,"user wins")
		

