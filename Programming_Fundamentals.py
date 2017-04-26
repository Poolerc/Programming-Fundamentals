#This program displays a letter grade based on numeric grade
grade=float(input("please enter your grade: "))
if(grade<60):
	print("Your grade is an F.")
elif(grade>=60 and grade<70):
	print("Your grade is an D.")
elif(grade>=70 and grade<80):
	print("Your grade is an C.")
elif(grade>=80 and grade<90):
	print("Your grade is an B.")
elif(grade>=90):
	print("Your grade is an A.")

