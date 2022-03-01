#Assignment 4

#Question 1
'''Program to solve the problem of  Tower Of Hanoi'''

print("\n\tTOWER OF HANOI\n")

# Defining a function for movement of rods in Tower of Hanoi.
def TowerOfHanoi(n, str_rod, tar_rod, helper_rod):
    if n == 1:
        print("Move disk 1 from rod", str_rod, "to rod", tar_rod)
        return
    TowerOfHanoi(n - 1, str_rod, helper_rod, tar_rod)
    print("Move disk", n, "from rod", str_rod, "to rod", tar_rod)
    TowerOfHanoi(n - 1, helper_rod, tar_rod, str_rod)

#Taking input from user for number of disks
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')

print("*"*90)

#Question 2
'''Program to print Pascal's triangle using both recursive and iterative procedures'''

print("\n\tPASCAL's TRIANGLE\n")

#Using recursive approach
print("\n\t Using Recursive Approach.\n")

def triangle_row(spaces, num_list):
    n_list = []
    n_list.append(1)
    if len(num_list) >= 2:
        for i in range(len(num_list) - 1):
            n_list.append(num_list[i] + num_list[i + 1])
    if len(num_list) >= 1:
        n_list.append(1)

    print("{:>4}".format(" ") * spaces, end='')
    for num in n_list:
        print("{:^7}".format(num), end=" ")
    spaces -= 1
    print()
    if spaces >= 0:
        triangle_row(spaces, n_list)

#Taking input from user to determine the number of rows of triangle.
rows = int(input("Enter number of rows: "))
num_list = []
triangle_row(rows - 1, num_list)

# Iterative Procedure.

print("\n\tIterative Procedure\n")

#Taking input from user to determine the number of rows of triangle.
no_of_rows = int(input("Enter the number of rows you want: "))

# Condition to check if the no of rows entered are positive or not
if no_of_rows < 0:
    print("Error!: Number of rows cannot be -ve.")
    exit()

arr = [[1]]

while len(arr) < no_of_rows:

    new_row = [1]
    last_row = arr[-1]

    for i in range(len(last_row) - 1):
        new_row.append(last_row[i] + last_row[i + 1])

    new_row += [1]
    arr.append(new_row)

#Making the triangle
width = len(str(arr[-1])) - 2
for i in arr:
    strng = ""

    for j in i:
        strng += (f"{j}" + "   ")

    print(strng.center(width * 2, " "))

print("*"*90)

#Question 3
'''Program to find quotient, remainder and using built-in function'''

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

# ensuring that denominator is not zero
while b == 0:
    b = int(input("Denominator cannot be zero. Please enter a non zero number : "))

Q, R = divmod(a, b)
m = [Q, R]


def division():
    Q, R = divmod(a, b)
    print(f"Quotient:{Q}\nRemainder:{R}")


division()

print('a)')
print(callable(division))

print('b)')
if all(divmod(a, b)):
    print('All the values are non zero')
else:
    print('All the values are not non zero')

print('c)')
m.extend([4, 5, 6])
print("After adding 4,5,6 : ", m)
filtered = filter(lambda n: n > 4, m)
print("Values greater than 4 are : ", list(filtered))

print('d)')
s = set(m)
print(s)

print('e)')
f_s = frozenset(s)
print("Immutable set : ", f_s)

print('f)')
m = max(f_s)
print("Hash value as a string is: ",hash(str(m)))
print("Hash value as an integer is: ",hash(m))


print("*"*90)

#Question 4
'''Using __init__ and __del__ function'''

#Creating a class
class Student:

    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
        print(f'Record for {self.name} is created\n')

    def __del__(self):
        print(f'Record for {self.name} is destroyed')

#Inputing student details
name = input("Enter name of student: ").strip()
roll_no = int(input("Enter SID of %s: " % (name)))
student1 = Student(name,roll_no)

print("The name of the student is %s and his/her roll number is %d" % (student1.name,student1.rno))

print(f'\nRecord for {student1.name} is destroyed')

print("*"*90)

#Question 5
'''Creating a class and storing employee data'''

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        print("%s has a salary of %d rupees" % (name,salary))

print("The data is stored where: ")
employee1 = Employee("Mehak",40000)
employee2 = Employee("Ashok",50000)
employee3 = Employee("Viren",60000)

#Updating Mehak's salary
print("\n(a) Updated the salary of %s from %d to " % (employee1.name,employee1.salary), end = "")
employee1.salary = 70000
print(employee1.salary)

#Deleting Viren's salary
print("\n(b)The record of {} is deleted".format(employee3.name))
del employee3

print("*"*90)

#Question 6
'''Program to check the friendship of Barbie and George'''


#input of words uttered by both Barbie and George
George = input("Word uttered by george: ").lower().strip()
Barbie = input("Word uttered by barbie: ").lower().strip()

#Defining a Function to get all the possible combinations of a word.
def word(s):
    if s == "":
        return [s]
    else:
        ans = []
        for w in word(s[1:]):
            for pos in range(len(w) + 1):
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans

if len(George) == 0:
    print("Error! George have to say something")
else:
    if Barbie in word(George):
        print("True Friendship")

    else:
        print("False Friendship")

print("*************************************************************************END OF ASSIGNMENT*************************************************************************")
