m1=int(input("Enter the m1 mark:"))
m2=int(input("Enter the m2 mark:"))
m3=int(input("Enter the m3 mark:"))
m4=int(input("Enter the m4 mark:"))
m5=int(input("Enter the m5 mark:"))
total=m1+m2+m3+m4+m5
max=500;
if(total>=max):
	print("A Grade");
elif(total>400):
	print("Bgrade Grade");
elif(total>300):
	print("C Grade");
elif(total>250):
	print("D Grade");
else:
	print("You got Fail")
