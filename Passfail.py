x = int(input("enter obtained marks: "))
y = int(input("enter total marks: "))

percentage = x * 100 / y

if (40 <= percentage <=100):
	print("Pass")
if (0 <= percentage < 40 ):
	print("Fail")
else:
	print("Invalid Number")