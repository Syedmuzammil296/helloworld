x = int(input("Enter the value of Angle 1: "))
y = int(input("Enter the value of Angle 2: "))
z = int(input("Enter the value of Angle 3: "))


if x + y + z == 180:
	if (x == y == z):
		print("Equilateral Trianle")
	elif x == y or y == z or z == x:
		print("Isosceles Triangle")
	else: 
		print("scalene")
else:
	print("Invalid triangle: The sum of angles should be 180 degrees.")