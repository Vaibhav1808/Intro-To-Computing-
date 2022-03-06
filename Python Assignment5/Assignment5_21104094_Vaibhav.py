# Assignment 5

from tkinter import *
from tkinter import messagebox

# Question 1.
'''Program to make a GUI-based GST Tax Finding Calculator.'''

def calculation():
    """A function to calculate GST rate and total tax."""

    # Defining global variables for GST calculation.
    global original_cost, net_price, gst_rate, difference

    # If empty value is given, prompt an error window.
    if len(en1.get()) == 0 or len(en2.get()) == 0:
        messagebox.showerror("Error", "No value has been entered by the user.")

    else:
        # Creating an exception if any error occurs.
        try:
            original_cost = float(en1.get())
            net_price = float(en2.get())
            difference = net_price - original_cost
            gst_rate = (difference * 100) / original_cost

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # If original cost is greater than net price prompting an error window.
        if original_cost > net_price:
            q = messagebox.askokcancel("Warning",
                                       "The value of Original Cost is given greater than Net Price.\
                                       Do you wish to continue?")

            # If user selects ok displaying the result.
            if q:
                lb3.config(
                    text="Result :\n\nCalculated GST rate : {0:.2f}%\nTotal tax on Net Price : ₹{1:.2f}".format(
                        gst_rate,
                        difference))
                lb3.grid(row=3, columnspan=2, pady=10)
            else:
                pass
        else:
            lb3.config(
                text="Result :\n\nCalculated GST rate : {0:.2f}%\nTotal tax on Net Price : ₹{1:.2f}".format(
                    gst_rate,
                    difference))
            lb3.grid(row=3, columnspan=2, pady=10)


root1 = Tk()

# Title and icon
root1.title("Question 1")

# Geometry
root1.geometry('500x400')
root1.minsize(450, 370)
root1.maxsize(700, 450)

# Background Color
root1['bg'] = 'lemonchiffon'

# Heading
Heading = Label(root1, text="GST Tax Finding Calculator", bd=5, font=('Lucida Bright', 22, 'bold'), bg='lemonchiffon', fg='black')
Heading.pack(pady=10, ipadx=10)

# Creating a frame
f1 = Frame(root1, bd=20)
f1.pack()

# Content
lb1 = Label(f1, text="Original Cost: ", font=('Lucida Bright', 12))
lb1.grid(row=0, column=0, pady=10)


en1 = Entry(f1, font=('Lucida Bright', 12))
en1.grid(row=0, column=1, pady=10)


lb2 = Label(f1, text="Net Price: ", font=('Lucida Bright', 12))
lb2.grid(row=1, column=0, pady=10)


en2 = Entry(f1, font=('Lucida Bright', 12))
en2.grid(row=1, column=1, pady=10)


bt1 = Button(f1, text="Calculate", command=calculation, cursor='hand2', font=('Lucida Bright', 12))
bt1.grid(row=2, columnspan=2, pady=10)


lb3 = Label(f1, bg='grey', fg='white', font=('Lucida Bright', 12), bd=7)

root1.mainloop()

print()

# Question 2
'''Program to make a GUI-based GST Tax Finding Calculator.'''
from tkinter import *
from tkinter import messagebox
import calendar


def calender():
    """Defining a function to Create a separate window to display the calendar."""

    global year                                                                                                         # Defining a global variable.

    try:
        int(en1.get())
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Prompting Error if user enters no input
    if len(en1.get()) == 0:
        messagebox.showerror("Error", "No value has been entered for year.")

    elif int(en1.get()) <= 0:
        messagebox.showerror("Error", " Year cannot be -ve or 0.")

    else:
        # Creating an exception if invalid integer is entered by the user
        try:
            year = int(en1.get())                                                                                       # Getting value from entry box 1.

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # Using calendar library to print the Calendar
        cal = calendar.calendar(year)

        # Creating a different window to print Calendar
        top1 = Toplevel(root2)

        # Title and icon.
        top1.title(f"{year} Calender")

        # Geometry
        top1.geometry('640x620')
        top1.minsize(640, 630)
        top1.maxsize(640, 630)

        # Content

        # Text box 1
        txt1 = Text(top1, relief=GROOVE, borderwidth=2, width=100, height=100)
        txt1.pack(padx=20, pady=10)

        # Inserting calendar string in Text box 1
        txt1.insert('end', cal)

        top1.mainloop()


root2 = Tk()

# Title
root2.title("Question 2")

# Geometry
root2.geometry('400x300')
root2.minsize(350, 250)
root2.maxsize(500, 400)

# Background Color
root2['bg'] = 'PeachPuff2'

# Heading
Heading = Label(root2, text="Calender Application", bd=5, font=('Lucida Bright', 22, 'bold'), bg='PeachPuff2', fg='black')
Heading.pack(pady=10, ipadx=10)

# Creating a frame
f1 = Frame(root2, bd=20)
f1.pack()

# Content

# Label 1
lb1 = Label(f1, text="Enter year :", font=('Lucida Bright', 12))
lb1.pack(pady=5)

# Entry box 1
en1 = Entry(f1, font=('Lucida Bright', 12))
en1.pack(pady=5)

# Button 1
bt1 = Button(f1, text="Show Calender", command=calender, cursor='hand2', font=('Lucida Bright', 12))
bt1.pack(pady=5)


root2.mainloop()

print()

# Question 3.
'''Program to create a GUI-based calculator.'''

from tkinter import *
from tkinter import messagebox


def btn(e):
    """Defining a function to perform functions
        when any of the button is pressed."""

    # Defining a global variable
    global val

    text = e.widget.cget("text")

    # If '=' button is pressed calculating the result
    if text == "=":

        if val.get().isdigit():
            try:
                value = eval(val.get())
            except Exception as exp:
                messagebox.showerror("Error", str(exp))
                value = "Error"
        else:
            try:
                value = eval(cal_screen.get())
            except Exception as exp:
                value = "Error"
                messagebox.showerror("Error", str(exp))

        # Setting the value of entry box to the result
        val.set(value)
        # Updating the Entry box.
        cal_screen.update()

    # If 'C' button is pressed clearing the screen
    elif text == 'C':
        val.set("")
        root3.update()

    else:
        val.set(str(val.get()) + str(text))
        cal_screen.update()


def equals(n):
    """Defining a function which calculates the
        result when user presses Enter."""

    # Same as '=' condition above.
    if val.get().isdigit():
        try:
            value = eval(val.get())
        except Exception as exp:
            messagebox.showerror("Error", str(exp))
            value = "Error"
    else:
        try:
            value = eval(cal_screen.get())
        except Exception as exp:
            value = "Error"
            messagebox.showerror("Error", str(exp))

    val.set(value)
    cal_screen.update()


root3 = Tk()

# Title
root3.title("Question 3")

# Geometry
root3.geometry('500x650')
root3.minsize(425, 620)

# Background Color
root3['bg'] = 'burlywood3'

# Heading
Heading = Label(root3, text="Calculator", bd=5, font=('Lucida Bright', 22, 'bold'), bg='burlywood3', fg='black')
Heading.pack(pady=10, ipadx=10)

# Content

# val(a String variable for entry box)
val = StringVar()

# setting val's value to ""
val.set("")

# cal_screen - Entry box for calculator input
cal_screen = Entry(root3, textvariable=val, font=('Lucida Bright', 30, 'bold'), width=19)
cal_screen.pack(fill=X, padx=25)
cal_screen.bind('<Return>', equals)

# Frame 1
f1 = Frame(root3, bg='AntiqueWhite2')
f1.pack(pady=10, fill=BOTH, padx=25, side=TOP)

# Creating Buttons
bt1 = Button(f1, text="C", font=('Lucida Bright', 25, 'bold'), width=3)
bt2 = Button(f1, text="/", font=('Lucida Bright', 25, 'bold'), width=3)
bt3 = Button(f1, text="*", font=('Lucida Bright', 25, 'bold'), width=3)
bt4 = Button(f1, text="-", font=('Lucida Bright', 25, 'bold'), width=3)
bt5 = Button(f1, text=7, font=('Lucida Bright', 25, 'bold'), width=3)
bt6 = Button(f1, text=8, font=('Lucida Bright', 25, 'bold'), width=3)
bt7 = Button(f1, text=9, font=('Lucida Bright', 25, 'bold'), width=3)
bt8 = Button(f1, text="+", font=('Lucida Bright', 25, 'bold'), height=4, width=3)
bt9 = Button(f1, text=4, font=('Lucida Bright', 25, 'bold'), width=3)
bt10 = Button(f1, text=5, font=('Lucida Bright', 25, 'bold'), width=3)
bt11 = Button(f1, text=6, font=('Lucida Bright', 25, 'bold'), width=3)
bt12 = Button(f1, text=1, font=('Lucida Bright', 25, 'bold'), width=3)
bt13 = Button(f1, text=2, font=('Lucida Bright', 25, 'bold'), width=3)
bt14 = Button(f1, text=3, font=('Lucida Bright', 25, 'bold'), width=3)
bt15 = Button(f1, text="=", font=('Lucida Bright', 25, 'bold'), height=4, width=3)
bt16 = Button(f1, text=0, font=('Lucida Bright', 25, 'bold'), width=8)
bt17 = Button(f1, text=".", font=('Lucida Bright', 25, 'bold'), width=3)

# Grid Configuring
Grid.columnconfigure(f1, 0, weight=1)
Grid.columnconfigure(f1, 6, weight=1)

# Griding all the buttons
bt1.grid(row=0, column=1, padx=10, pady=10)
bt2.grid(row=0, column=2, padx=10, pady=10)
bt3.grid(row=0, column=3, padx=10, pady=10)
bt4.grid(row=0, column=4, padx=10, pady=10)
bt5.grid(row=1, column=1, padx=10, pady=10)
bt6.grid(row=1, column=2, padx=10, pady=10)
bt7.grid(row=1, column=3, padx=10, pady=10)
bt8.grid(row=1, column=4, columnspan=2, rowspan=2, padx=10, pady=10)
bt9.grid(row=2, column=1, padx=10, pady=10)
bt10.grid(row=2, column=2, padx=10, pady=10)
bt11.grid(row=2, column=3, padx=10, pady=10)
bt12.grid(row=3, column=1, padx=10, pady=10)
bt13.grid(row=3, column=2, padx=10, pady=10)
bt14.grid(row=3, column=3, padx=10, pady=10)
bt15.grid(row=3, column=4, columnspan=2, rowspan=2, padx=10, pady=10)
bt16.grid(row=4, column=1, columnspan=2, rowspan=2, padx=10, pady=10)
bt17.grid(row=4, column=3, padx=10, pady=10)

# Binding all the buttons to functions
bt1.bind("<Button-1>", btn)
bt2.bind("<Button-1>", btn)
bt3.bind("<Button-1>", btn)
bt4.bind("<Button-1>", btn)
bt5.bind("<Button-1>", btn)
bt6.bind("<Button-1>", btn)
bt7.bind("<Button-1>", btn)
bt8.bind("<Button-1>", btn)
bt9.bind("<Button-1>", btn)
bt10.bind("<Button-1>", btn)
bt11.bind("<Button-1>", btn)
bt12.bind("<Button-1>", btn)
bt13.bind("<Button-1>", btn)
bt14.bind("<Button-1>", btn)
bt15.bind("<Button-1>", btn)
bt16.bind("<Button-1>", btn)
bt17.bind("<Button-1>", btn)

root3.mainloop()

print()

# Question 4
'''Program for quick sorting a list of marks.'''

# Defining Quicksort for l
def quicksort(array, left, right):
    if left < right:
        partition_pos = partition(array, left, right)  # Partition_pos is position from where to part list.

        quicksort(array, left, partition_pos - 1)
        quicksort(array, partition_pos + 1, right)


# Defining Partition function for quick sorting
def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:

        while i < right and array[i] < pivot:
            i += 1
        while j > left and array[j] >= pivot:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]  # Interchanging elements of array.

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]  # Interchanging element and pivot.

    return i

print("Question 4")
      
# asking user to input number of students and their marks
while True:
    try:
        num_of_students = int(input("\nEnter the number of students: "))
        if num_of_students <= 0:
            print("\nPlease enter a positive integeral value!\n")

            continue
        else:
            break

    except ValueError:
        print("\nPlease enter a positive integeral value only!\n")

List_of_num = []

print()

# appending all student's numbers in a list
for k in range(1, num_of_students + 1):
    List_of_num.append(int(input("Enter the marks of student {}: ".format(k))))

# Printing out the list of marks entered by the user
print("\nList of marks of Students entered by the User is:", List_of_num)

quicksort(List_of_num, 0, len(List_of_num) - 1)

# Printing out the list after quick sorting
print("List of marks of Students after quick sorting is:", List_of_num)

print("*"*90)

# Question 5
'''Python Script for creating an integer array.'''

print("\nQuestion 5")

def Binary_Search(arr, n, low, high):
    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            return Binary_Search(arr, n, mid + 1, high)

        else:
            return Binary_Search(arr, n, low, mid - 1)

    else:
        return False


n = list(map(int, input("\nEnter all numbers with spaces between them: ").split()))

n.sort()

print("\npart(a). Sorting the inputted array",n)

a = int(input("\nWhich number's index do you want to know?: "))

if a in n:
    result = Binary_Search(n, a, 0, len(n))
    if result != False:
        print("\npart(b). The number {} is found at index number {}.".format(a, str(result)))
    else:
        pass
else:
    print(f"\npart(b). Number {a}, is not in the list!")

print(f"part(c). Number {a} is occurred {n.count(a)} times in the given list.")

print("*****************************************************************END OF ASSIGNMENT*****************************************************************")