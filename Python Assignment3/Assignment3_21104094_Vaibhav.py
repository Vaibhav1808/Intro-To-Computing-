#Assignment 3

#Question 1
'''Program to count the number of occurrences'''

user_string = input("Enter the string: ")

string_entered = user_string.lower().split()

#Counting occurances of characters if a single word is entered by the user
if " " not in user_string:
    string_entered = string_entered[0]

occurances = {}

for letter in string_entered:
    if letter in occurances:
        occurances[letter] += 1
    else:
        occurances[letter] = 1
#Counting occurances of words if a sentence is entered by the user
else:
    list=[]
    for word in string_entered:
        count = string_entered.count(word)
        list.append(f"Occurances of {word}: {count}")
for o in set(list):
    print(o)

print("*"*90)

#Question 2
'''Program to print next date of input date..'''

 #Taking input from user
day = int(input("Please enter Date: "))
month = int(input("Please enter Month: "))
year = int(input("Please enter Year: "))

# Checking for all the invalid cases and removing them
if day > 30 and month in {2, 4, 6, 9, 11}:
    condition = False
elif day > 31 and month in {1, 3, 5, 7, 8, 10, 12}:
    condition = False
elif (day == 29 or day == 30) and month == 2 and year % 4 != 0:
    condition = False
elif day == 30 and month == 2 and year % 4 == 0:
    condition = False
elif day <= 0 or month <= 0 or year > 2025 or year < 1800:
    condition = False
else:
    condition = True

if condition:
    # checking and changing for the last day of a year
    if day == 31 and month == 12:
        next_year = year + 1
    else:
        next_year = year
    if month == 12 and day == 31:
        next_month = 1
    else:
        next_month = month

    # checking for months with 31 days
    if month in {1, 3, 5, 7, 8, 10, 12}:
        if day == 31:
            next_day = 1
            if month != 12:
                next_month = month + 1
            else:
                next_month = 1
        else:
            next_day = day + 1

    # checking for the month of february
    elif month == 2:
        if year % 4 == 0:
            if day == 29:
                next_day = 1
                next_month = 3
            else:
                next_day = day + 1
        else:
            if day == 28:
                next_day = 1
                next_month = 3
            else:
                next_day = day + 1

    # covering rest of the cases
    else:
        if day == 30:
            next_day = 1
            next_month = month + 1
        else:
            next_day = day + 1
    print(f"Next Date is: {next_day}/{next_month}/{next_year}")
else:
    # gives a warning and ends the program
    print("That's not a valid date")

print("*"*90)

#Question 3
'''Program to get the square of the number entered by user in a tuple'''

nums=input("Enter desired numbers with spaces between them: ")
list=nums.split()

#defining an empty list to store tuple pairs for later use
list2=[]
for i in list:
    list2.append((int(i),int(i)**2))
print("Pairs of entered numbers and their squares are: ", list2)

print("*"*90)

#Question 4
'''Program to show the grade of a student'''

grade=int(input("Enter Grade Points: "))

#Storing the given table in a dictionary
grade_table ={10:{'grade_input':'A+','remarks':'Outstanding'},
           9:{'grade_input':'A','remarks':'Excellent'},
           8:{'grade_input':'B+','remarks':'Very Good'},
           7:{'grade_input':'B','remarks':'Good'},
           6:{'grade_input':'C+','remarks':'Average'},
           5:{'grade_input':'C','remarks':'Below Average'},
           4:{'grade_input':'D','remarks':'Poor'}}

if 3<grade<11:
    for key in grade_table.keys():
        if key == grade:
            value = grade_table[key]
            print(f"Your Grade is {value['grade_input']} and {value['remarks']} performance ")
        else:
            continue
else:
    print("Error! You entered an invalid grade")

print("*"*90)

#Question 5
'''Program to print the given pattern'''

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

for row in range(0,6):
    column=0
    counter=0
    while column<11:
        if column<row or column>11-row-1:
            print(" ", end="")

        else:
            print(letters[counter], end="")
            counter=counter+1
        column=column+1
    print("")

print("*"*90)

#Question 6

condition=True

#Defining dictionary to store the values
Dictionary={}
prompt="y"
while condition:
    if prompt.lower()=="y":
        name=input("Please enter the name of the Student: ")
        SID = int(input("Please Enter SID of Student: "))
        Dictionary[SID]=name
        prompt= input("If you want to enter more details press Y/N: ")
        condition = True

    else:
        condition = False
print("")

print("Part (a)")
for key,value in Dictionary.items():
    print(f"{key} : {value}")
print("")

print("Part (b)")
Val_sort_dict= sorted(Dictionary.values())
Name_sort = {}


def get_key(val, dicti):
    for key, value in dicti.items():
        if val == value:
            return key


for s_name in Val_sort_dict:
    s_sid = get_key(s_name, Dictionary)
    Name_sort[s_sid] = s_name

print(Name_sort)

print("")

print("Part (c)")
Key_sort_dict= sorted(Dictionary.keys())
dict={}

for i in Key_sort_dict:
    dict[i]=Dictionary[i]
print(dict)
print("")

print("Part (d)")
sid=int(input("Please enter the student's SID whose detail you need: "))
if sid in Dictionary.keys():
    print(f"Name of the required student is {Dictionary[sid]}")
else:
    print("The SID is not present in the given Data")
print("")

print("*"*90)

#Question 7
'''Program to print Fibonacci sequence and its average'''

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n < 0:
        return "Number of terms must be non-negative\nPlease enter again\n"
    elif n == 0:
        return "As the number of terms = 0, the average of all terms = 0"
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Enter the no. of terms of the Fibonacci sequence: "))

sum = 0

for i in range(1, num + 1):
    print(fibonacci(i), end=" ")

    sum += fibonacci(i)

print("\nThe average of the terms of Fibonacci sequence upto %d terms is %0.2f" % (num,sum/num))

print("*"*90)

#Question 8

Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#Finding symmetric difference of both the sets
print("Part (a)")
set_notboth=Set1^Set2
print(f"Set with elements not common in both is {set_notboth}")

#Finding symmetric difference of all sets
print("Part (b)")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that is only present in one set is {set_onlyinone}")

#Finding elements that is common in any two sets
print("Part (c)")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that is only present in two set is {set_onlyintwo}")

#Finding elements common in set1 and range 1 to 10
print("Part (d)")
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common_1=new_set1- Set1
print(f"Set of all integers in the range 1 to 10 that are not in Set1 {not_common_1}")

#Finding elements common in sets 1,2,3 and range 1 to 10
print("Part (e)")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3 {not_common_2}")
print("")


print("************************************END OF ASSIGNMENT************************************")

