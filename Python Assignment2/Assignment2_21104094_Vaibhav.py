#Assignment 2


#Question 1
'''Performing different operations on string.'''

print("\nString Operations\n")

#Now, storing the given string in a variable named string
string = "Python is a case sensitive language"

#Printing out the given string
print("The original String is:",string)

#1(a) Finding the length of the given string using the length function
length = len(string)

#Printing its length
print("\tlength of the given string:",length)


#1(b) Printing the string in reverse order using slicing.
print("\tString in reversed order is:",string[::-1])


#1(c) Slicing the string and storing the value in a new variable named new_string
new_string = string[10:26]

#Now, printing the sliced string
print("\tNew String:",new_string)


#1(d) Replacing words in string using replace command and printing out the modified string
print("\tThe modified string is:",string.replace("a case sensitive","object oriented"))

#1(e) Finding the index of 'a'
print("\tIndex of 'a' in the given string:",string.find("a"))


#1(f) Removing the white spaces from the string
print("\tString after removing the white spaces:",string.replace(" ",""))

print("*"*90)


#Question 2
'''Program to do String Formatting.'''

print("\nString Formatting\n")

#Taking inputs from user
name = input("Enter your Name:")
sid = input("Enter your SID:")  
dept_name = input("Enter the name of your department:") 
cgpa = input("Enter your CGPA:")    

print()

#Printing the Strings by using .format command
print("Hey {0} Here!\
    \nMy SID is {1}\
    \nI am from {2} department and my CGPA is {3}.".format(name, sid, dept_name, cgpa))


print("*"*90)


#Question 3
'''Program to use Bitwise Operators.'''

print("\nBitwise Operators\n")

#The values of variables a and b as assigned to us
a = 56
b = 10

#printing out the variables
print("a:",a)
print("b:",b)
 
print()

#3(a)
#Using AND operator

print("a&b:",a&b)

#3(b)
#Using OR operator

print("a|b:",a|b)

#3(c)
#Using XOR operator

print("a^b:",a^b)

#3(d)
#Performing left bit shifting

print("Left shifting both a and b by 2 bits:",a << 2,b << 2)

#3(e)
#Performing right bit shifting

print("Right shifting a by 2 and b with 4 bits:",a >> 2,b >> 4)

print("*"*90)


#Question 4
'''Program to find Greatest Number.'''


print("\nGreatest Number Calculator\n")

#Taking inputs of numbers from users
num1 = float(input("Enter your first number:"))
num2 = float(input("Enter your second number:"))
num3 = float(input("Enter your third number:"))

#Using conditional statements to find the greatest number entered by the user
if (num1 >= num2) and (num1 >= num3):
    greatest_num = num1 
elif (num2 >= num1) and (num2 >= num3): 
    greatest_num = num2
else:   
    greatest_num = num3

#Now, printing the greatest of the three numbers
print("Greatest of the three numbers entered by the user :",greatest_num)

print("*"*90)


#Question 5
'''Program to compare Strings.'''

print("\nString Scanner\n")

#Taking input from the user and storing it in a variable named your_string
your_string = input("Enter the String:")

#Using conditional statement to check if "name" is present or not in your_string
if "name" in your_string:    
    print("Yes")    
else:   
    print("No") 

print("*"*90)


#Question 6
'''Program to Check Validity of a Triangle.'''

print("\nTriangle Sides Validity Checker\n")

#Taking input of side side1,side2 and side3 from the user
side1 = (input("Enter the Length of first side:"))
side2 = (input("Enter the Length of second side:"))
side3 = (input("Enter the Length of third side:"))

#Using conditional statements to put a condition on sides of triangle


#condition to check the validity of triangle i.e. any of the three lengths is greater than the sum of other two
if (int(side1) + int(side2) <= int(side3)) or (int(side1) + int(side3) <= int(side2)) or (int(side2) + int(side3) <= int(side1)):
    print("No")
else:
    print("Yes")

print("*************************************END OF ASSIGNMENT*************************************")


