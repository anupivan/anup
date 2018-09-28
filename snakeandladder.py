#snake and ladder
import random
count=0
while(count<=100):
	i=input("enter r to roll")
	if(i=='r'):
		i=random.randint(1,6)
		count=count+i
		print("my position",count)
		print("random value",i)

	if(count==11):
		count=2
		print("oops snake bit you")
		print("my position",count)
	elif(count==25):
		count=4
		print("oops snake bit you")
		print("my position",count)
	elif(count==38):
		count=9
		print("oops snake bit you")
		print("my position",count)
	elif(count==65):
		count=46
		print("oops snake bit you")
		print("my position",count)
	elif(count==89):
		count=70
		print("oops snake bit you")
		print("my position",count)
	elif(count==93):
		count=64
		print("oops snake bit you")
		print("my position",count)
	elif(count==8):
		count=37
		print("wow you got a ladder")
		print("my position",count)
	elif(count==13):
		count=34
		print("wow you got a ladder")
		print("my position",count)
	elif(count==40):
		count=68
		print("wow you got a ladder")
		print("my position",count)
	elif(count==52):
		count=81
		print("wow you got a ladder")
		print("my position",count)
	elif(count==76):
		count=97
		print("wow you got a ladder")
		print("my position",count)
	elif(count>100):
		count=count-r
		print("cannot go beyond 100")
	elif(count==100):
		print("your the winner")
		break
		
		