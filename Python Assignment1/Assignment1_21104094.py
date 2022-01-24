#Assignment 1

#Question 1

print("\n Welcome to Average Calculator\n")

#Taking input values from the user

num1= float(input("Enter First Number: "))
num2= float(input("Enter Second Number: "))
num3= float(input("Enter Third Number: "))

#Now calculating the average of these numbers
result= (num1+num2+num3)/3
print("The average of these numbers is:", result )

print("\n","*"*70)

#**********Question2**********
'''Program to compute Income Tax'''

print("\n Welcome to Income Tax Calculator\n")

#Taking the input of gross income and number of dependents from the user
gross_income= float(input("Enter your Gross Income in $(Round off to nearest penny):"))
dependents= int(input("Enter the number of Dependents:"))

#Now, Calculating the taxable income and total income tax
std_deduction= 10000
dep_deduction= 3000
taxable_income= gross_income-std_deduction-(dep_deduction*dependents)
tax= taxable_income*(20/100)

#Printing the total income tax to be paid
print("Your total calculated income tax is $",tax)

print("\n","*"*70)

#**********Question3**********
'''Storing different datatypes in a list'''

#Taking input data from user

SID= int(input("Enter your SID: " ))
name= str(input("Enter your name: "))
gender= str(input("Enter your gender(M-Male, F-Female, U-Unknown): "))
course_name= str(input("Enter your course name: "))
cgpa= float(input("Enter your CGPA: "))

#Converting the data by user into a list
student= [SID,name,course_name,cgpa]

print("student info:" , student)

print("\n","*"*70)

#**********Question4**********

'''Entering marks of 5 students and displaying them in sorting manner'''

#Taking input from the user
n1= float(input("Enter marks of student1: "))
n2= float(input("Enter marks of student2: "))
n3= float(input("Enter marks of student3: "))
n4= float(input("Enter marks of student4: "))
n5= float(input("Enter marks of student5: "))

#Now, converting the user input into list
marks= [n1,n2,n3,n4,n5]

#Sorting the marks given
marks.sort()
print("Marks in ascending order ", marks)

marks.reverse()
print("Marks in descending order ", marks)

print("\n","*"*70)

#**********Question5**********
'''Removing a specific element from the list'''

list1= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print("color",list1)

#(a) removing the 4th element from the list
list1.pop(3)
print("color",list1)

#(b) replacing 'Black' and 'Pink' from 'Purple'
list2= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list2[3:5] = ['Purple']
print("The modified list is ", list2)

print("\n","*"*70)

#********************END OF ASSIGNMENT**************************
