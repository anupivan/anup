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
		
		
		
		output=enter r to rollr
my position 1
random value 1
enter r to rollr
my position 2
random value 1
enter r to rollr
my position 7
random value 5
enter r to rollr
my position 8
random value 1
wow you got a ladder
my position 37
enter r to rollr
my position 38
random value 1
oops snake bit you
my position 9
enter r to roll
enter r to rollr
my position 14
random value 5
enter r to rollr
my position 18
random value 4
enter r to rollr
my position 20
random value 2
enter r to rollr
my position 26
random value 6
enter r to rollr
my position 31
random value 5
enter r to rollr
my position 34
random value 3
enter r to rollr
my position 37
random value 3
enter r to rollr
my position 39
random value 2
enter r to rollr
my position 42
random value 3
enter r to rollr
my position 43
random value 1
enter r to rollr
my position 46
random value 3
enter r to rollr
my position 51
random value 5
enter r to rollr
my position 54
random value 3
enter r to rollr
my position 59
random value 5
enter r to rollr
my position 64
random value 5
enter r to rollr
my position 67
random value 3
enter r to rollr
my position 71
random value 4
enter r to rollr
my position 72
random value 1
enter r to rollr
my position 74
random value 2
enter r to rollr
my position 79
random value 5
enter r to rollr
my position 80
random value 1
enter r to rollr
my position 86
random value 6
enter r to rollr
my position 91
random value 5
enter r to rollr
my position 92
random value 1
enter r to rollr
my position 94
random value 2
enter r to rollr
my position 100
random value 6
your the winner

		
		
