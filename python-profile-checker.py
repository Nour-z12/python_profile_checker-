name =input("enter your name: ")
age=int(input("enter your age: "))
gpa=float(input("enter your GPA 0-5: "))
field_of_interest=input("enter your field of interest: ")
graduated=input("have you graduated? (yes/no): ").lower()
if age<25 and gpa>=3.5 and graduated=="yes":
    print(f"{name}, you are eligible for the scholarship in {field_of_interest}.")
elif age<30 and gpa>=2.5:
    print(f"{name}, you are eligible for the internship in {field_of_interest}.")
else:
    print("please apply again later.")