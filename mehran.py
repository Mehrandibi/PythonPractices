#print("Python practices")
#write a program that does arithmetic addition and division


""" num1=float(input("Enter the first number: "))
num2=float(input("enter the second number: "))
addition=num1+num2
print(f"{num1} + {num2} = { addition}")
if num2==0:
    print("devision to 0 is impossible")
else:
    div=float(num1/num2)
print(f"{num1} devided by {num2} = {div}") """


#___________________________________________________________________
#write a program to compute area of a triangle
""" base=float(input("Enter the base : "))
height=float(input("enter the height : "))
area=base*height/2
print(f" Area is {area}") """

#___________________________________________________________________
#write a program that swaps two variables
""" numb1=input("Enter the first number : ")
numb2=input("Enter the second number : ")
print(f"The original numbers are {numb1} and {numb2}")
temp=numb1
numb1=numb2
numb2=temp

print(f"The swapped numbers are {numb1} and {numb2}") """

#___________________________________________________________________
#write a program that generates a random number
""" import random
print(f"Random numner: {random.randint(1,100)}") """
#___________________________________________________________________
#write a program that displays calendar
""" import calendar
year=int(input("Enter year: "))
month=int(input("Enter month as a two digit number: "))
cal=calendar.month(year,month)
print(cal)  """
# #print(month**2)
# #print(pow(month,2)) """
#___________________________________________________________________
#Swap two variables without temp var.
""" a=input("Enter the first number: ")
b=input("Enter the second number: ")
print(f"a and b are {a} and {b}.")
a,b=b,a
print(f"We swapped them without a temp var. a is now {a} and b is {b}") """
#______________________________________________________________________
#write a program that determines if n is a prime number:
""" n=int(input("enter the number: "))
flag=False
if n==1:
    print("1 is not a prime number.")
else:    
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is divisible to {i}. So, it is not a prime.")
            flag=True
            break
if flag==False:        
    print(f"{n} is a prime.") """
#______________________________________________________________________
#write a program that prints all prime numbers between 1 , a given number by the user!:
""" primes=[]
n=int(input("Enter th efinal number to give you a list of numbers that are prime and smaller than {n}: "))
for i in range (2,n):
    flag=False
    for k in range(2,i):
        if i%k==0:
            flag=True
            break
    if flag==False:
        primes.append(i)
print(f"The prime numbers between 1, 10 are: {primes}")
 """
#______________________________________________________________________
#write a program that prints the factorial of a given number:
""" n=int(input("Enter the n: "))
m=1
if n==0:
    m=1
else:    
    for i in range(1,n+1):
        m=i*m
print (f"{m} is {n}!")     """    

#______________________________________________________________________
#=Write a program that prints Fibonacci number of an input:
#n=int(input("Enter the n: "))

# if n==0 or n==1:
#     out=1
#     print(f"Fibonacci({n}) is ")
#     print(out)
# else:
#     for i in range(n):
        
#     # else:
#     #     out=Fib(n)+Fib(n-1)
#     #     print(f"Fibonacci({n}) is: {out}.")
#     #     return out
""" 

def fibonacci(n):
    if n <= 0:
        print("Input should be a positive integer.")
        return 100
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Number of Fibonacci numbers to generate
#n = 10

# Generating and printing the Fibonacci numbers
for i in range(1, n + 1):
    print(fibonacci(i))
 """

""" import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class PrimeNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Prime Number Generator')

        layout = QVBoxLayout()

        self.label = QLabel('Enter a number:')
        layout.addWidget(self.label)

        self.entry = QLineEdit(self)
        layout.addWidget(self.entry)

        self.button = QPushButton('Find Primes', self)
        self.button.clicked.connect(self.find_primes)
        layout.addWidget(self.button)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def find_primes(self):
        try:
            n = int(self.entry.text())
            primes = []
            for i in range(2, n):
                flag = False
                for k in range(2, i):
                    if i % k == 0:
                        flag = True
                        break
                if not flag:
                    primes.append(i)
            self.result_label.setText(f"Prime numbers less than {n}: {primes}")
        except ValueError:
            QMessageBox.critical(self, "Invalid input", "Please enter a valid integer.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PrimeNumberGenerator()
    ex.show()
    sys.exit(app.exec_()) """

""" import tkinter as tk
from tkinter import messagebox

def find_primes():
    try:
        n = int(entry.get())
        primes = []
        for i in range(2, n):
            flag = False
            for k in range(2, i):
                if i % k == 0:
                    flag = True
                    break
            if not flag:
                primes.append(i)
        result_label.config(text=f"Prime numbers less than {n}: {primes}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Prime Number Generator")

# Create and place the widgets
tk.Label(root, text="Enter a number:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Find Primes", command=find_primes).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

Run the application
root.mainloop() """
''' 
import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
pen = turtle.Turtle()
pen.speed(3)
pen.color("white")

# Function to draw the text "mateen"
def draw_text():
    pen.penup()
    pen.goto(-200, 0)
    pen.pendown()
    pen.color("cyan")
    pen.write("Mateen", font=("Arial", 80, "bold"), align="center")

# Function to draw a heart shape
def draw_heart(size):
    pen.begin_fill()
    pen.left(50)
    pen.forward(size)
    pen.circle(size / 2, 180)
    pen.right(100)
    pen.circle(size / 2, 180)
    pen.forward(size)
    pen.end_fill()

# Function to draw a cool effect around the text
def draw_effect():
    pen.penup()
    pen.goto(0, -150)
    pen.pendown()
    pen.color("red")
    pen.width(2)
    for _ in range(36):
        draw_heart(100)
        pen.right(10)

# Draw the text and the effect
draw_text()
draw_effect()

# Hide the turtle and display the window
pen.hideturtle()
turtle.done() '''
#------------------------
#Sum of cubes of first n natural numbers
''' 
def cube_sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        total = sum([i**3 for i in range(1, n + 1)])
    return total
# Input the number of natural numbers
n = int(input("Enter the value of n: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    result = cube_sum_of_natural_numbers(n)
print(f"The cube sum of the first {n} natural numbers is: {result}")


import tkinter as tk
from tkinter import messagebox

def cube_sum_of_natural_numbers(n):
    if n <= 0:
        return 0
    else:
        total = sum([i**3 for i in range(1, n + 1)])
    return total

def calculate_cube_sum():
    try:
        n = int(entry.get())
        if n <= 0:
            messagebox.showerror("Invalid input", "Please enter a positive integer.")
        else:
            result = cube_sum_of_natural_numbers(n)
            result_label.config(text=f"The cube sum of the first {n} natural numbers is: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Cube Sum of Natural Numbers")

# Create and place the widgets
tk.Label(root, text="Enter the value of n:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Calculate", command=calculate_cube_sum).pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=10) '''

# Run the application
#root.mainloop()
#------------------------
''' # Finding Sum of Array Using sum()
Inp = input("Enter an array (space-separated numbers): ").split()
#print(Inp)
Inp = [int(x) for x in Inp]
print(f"The sum is {sum(Inp)}") '''

#------------------------
#Write a Python Program to find largest element in an array.
''' def largest_element(arr):
    max_e = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_e:
            max_e = arr[i]
    return max_e       
def main():
    
    Inp = input("Enter an array (space-separated numbers): ").split()
    Inp = [int(x) for x in Inp]
    
    
    # Finding the largest element in the array
    largest = largest_element(Inp)
    print(f"The largest element is {largest}")

if __name__ == "__main__":
    main() '''
    
#------------------------
#Write a Python Program for array rotation.
''' def array_rotation(arr):
    n=len(arr)
    arr2=[]
    for i in range(n):
        arr2.append(arr[n-i-1])
    return arr2
def main():
    Inp = input("Enter an array (space-separated numbers): ").split()
    Inp = list([float(x) for x in Inp])
    rotated = array_rotation(Inp)
    #alternatively you could say  
    rotated2=Inp[::-1]
    print(f"The rotated array is {rotated} and {rotated2}")   
if __name__ == "__main__":
    main()
    
     '''
#------------------------
#Write a Python Program to Split the array and add the first part to the end?
''' def split_array(arr, k):
    n = len(arr)
    arr1 = arr[:k]
    arr2 = arr[k:]
    arr3 = arr2 + arr1
    return arr3
def main():
    Inp = input("Enter an array (space-separated numbers): ").split()
    Inp = list([float(x) for x in Inp])
    k = int(input("Enter the index at which to split: "))
    result = split_array(Inp, k)
    print(f"The split array is {result}")
if __name__ == "__main__":
    main() '''
#------------------------    
#Write a Python Program to Add Two Matrices.  
''' def add_matrices(mat1, mat2):
    result = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return result    
def main():
     # Define the dimensions of the matrices
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    mat1 = [[float(input(f"Enter element ({i + 1}, {j + 1}) of matrix 1: ")) for j in range(m)] for i in range(n)]
    mat2 = [[float(input(f"Enter element ({i + 1}, {j + 1}) of matrix 2: ")) for j in range(m)] for i in range(n)]
    matsum = add_matrices(mat1, mat2)
    print("The sum of the matrices is:")
    for row in matsum:
        print(row)
if __name__ == "__main__":
    main()
     '''
#------------------------    
#Write a Python Program to transpose a matrix:
''' def transpose_matrix(mat):
    result = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]
    return result   
def main():
    # Define the dimensions of the matrix
    n = int(input("Enter the number of rows: "))
    m = int(input("Enter the number of columns: "))
    mat = [[float(input(f"Enter element ({i + 1}, {j + 1}): ")) for j in range(m)] for i in range(n)]
    transposed = transpose_matrix(mat)
    print(f"The matrix is {mat} but the transposed matrix is {transposed}")
    #dimension of the matrices:
    x=len(mat)
    y= len(mat[0])
    xT=len(transposed)
    yT=len(transposed[0])
    print(f"The dimensions of the matrix is {x} and {y} but those of the transposed matrix are {xT} and {yT}")
if __name__ == "__main__":        
    main()                            
   '''
#------------------------   
''' # Program to sort alphabetically the words form a string provided by the user
def sortAlphabetically(str):
    words=input("Enter a string: ").split()
    words.sort()
    return words
def main():
    result = sortAlphabetically("str")
    print(f"The sorted words are: {result}") 
if __name__ == "__main__":
    main()
         '''
#------------------------
#Write a Python Program to Remove Punctuation From a String.
#def remove_punctuation(s):
#    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#    no_punct = ""
#    for char in s:
#        if char not in punctuations:
#            no_punct = no_punct + char
#    return no_punct    
#def main():
#    stringUser = input("Enter a string: ")
#    newStr=remove_punctuation(stringUser)
#    print(f"The string without punctuation is: {newStr}")
#    return newStr
#if __name__ == "__main__":
#    main()
#------------------------
#Write a Python Program to count the number of vowels in a string.
''' def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
def main():
    stringUser = input("Enter a string: ")
    numVowels=count_vowels(stringUser)
    print(f"The number of vowels in the string is: {numVowels}")
    return numVowels
if __name__ == "__main__":
    main()
#------------------------
#Write a Python Program to check if a string is palindrome or not.
def isPalindrome(s):
    for char in s:
        if s==s[::-1]:
            return True
        else:
            return False 
    
def main():
    stringUser = input("Enter a string: ")
    if isPalindrome(stringUser):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")   
if __name__ == "__main__":
    main() '''
#------------------------
#Write a Python Program to find the second largest number in a list.
''' def second_largest(arr):
    arr.sort()
    return arr[-2]
def main():
    Inp = input("Enter an array (space-separated numbers): ").split()
    Inp = [float(x) for x in Inp]
    second_largest_num = second_largest(Inp)
    print(f"The second largest number is {second_largest_num}")
if __name__ == "__main__":        
    main()  '''
#------------------------
''' #Write a Python Program to find the second smallest number in a list.
def second_smallest(arr):
    arr.sort()
    return arr[1]
 '''
#------------------------
#Write a Python Program to find the union of two lists.
''' def union_lists(list1, list2):
    union = list(set(list1) | set(list2))
    return  union       
def main():
    list1 = input("Enter the first list (space-separated numbers-no brackets): ").split()
    list1 = [float(x) for x in list1]
    list2 = input("Enter the second list (space-separated numbers-no brackets): ").split()
    list2 = [float(x) for x in list2]
    union = union_lists(list1, list2)
    print(f"The union of the two lists is: {union}")
if __name__ == "__main__":  
    main() 

    '''
#------------------------
#Write a Python Program to find the intersection of two lists.
''' def intersection_lists(list1, list2):
    intersection = list(set(list1) & set(list2))
    return intersection'''
#------------------------
#Write a Python program to check if the given number is a Disarium Number.
#A Disarium number is a number that is equal to the sum of its digits each raised to the
#power of its respective position. For example, 89 is a Disarium number because.
#+ = 8 + 81 = 89
''' def isDisarium(n):
    n_str = str(n)
    length = len(n_str)
    sum = 0
    for i in range(length):
        sum += int(n_str[i]) ** (i + 1)
    return sum == n '''
#def main():
#    n = int(input("Enter a number: "))
#    if isDisarium(n):
#        print(f"{n} is a Disarium number.")
#    else:
#        print(f"{n} is not a Disarium number.")
#if __name__ == "__main__":
#    main()
#------------------------
#Write a Python program to print all Disarium numbers between 1 to a number given by the user.
''' def disarium_numbers(n):
    #disariums = []
'''    '''  for i in range(1, n + 1):
        if isDisarium(i):
            disariums.append(i)
    return disariums  '''   '''   
#second way to write the function
    disariums = [num for num in range(1, n+1) if isDisarium(num)]
    return disariums
def main():
    n = int(input("Enter a number: "))
    disariums = disarium_numbers(n)
    print(f"The Disarium numbers between 1 and {n} are: {disariums}")
if __name__ == "__main__":
    main() '''
#------------------------
''' Write a Python program to check if the given number is Happy Number.
Happy Number: A Happy Number is a positive integer that, when you repeatedly replace
the number by the sum of the squares of its digits and continue the process, eventualy
reaches 1. If the process never reaches 1 but instead loops endlessly in a cycle, the number
is not a Happy Number.
For example:
19 is a Happy Number because:
The process reaches 1, so 19 is a Happy Number.
+ = 82
12 92
+ = 68
82 22
+ = 100
62 82
+ + = 1 '''
''' def sumDigits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit) ** 2
    return sum

def isHappy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sumDigits(n)
    return n == 1

#print all happy numbers between 1 and n
def happy_numbers(n):
    happy = [num for num in range(1, n+1) if isHappy(num)]
    return happy

def main():
    n = int(input("Enter a number: "))
    happy = happy_numbers(n)
    print(f"The Happy numbers between 1 and {n} are: {happy}")

''' 
''' def main():
    n = int(input("Enter a number: "))
    if isHappy(n):
        print(f"{n} is a Happy number.")
    else:
        print(f"{n} is not a Happy number.") '''
'''if __name__ == "__main__":
    main() '''
#------------------------
#Write a Python program to determine whether the given number is a Harshad Number.
#A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
#In other words, a number is considered a Harshad number if it can be evenly divided by the
#sum of its own digits.
#For example:
#18 is a Harshad number because , and 18 is divisible by 9
#42 is not a Harshad number because , and 42 is not divisible by 6.
''' def isHarshad(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return n % sum == 0

def main():   
    n = int(input("Enter a number: "))
    if isHarshad(n):
        print(f"{n} is a Harshad number.")
    else:
        print(f"{n} is not a Harshad number.") 
if __name__ == "__main__":
    main() '''
#------------------------
#Write a Python program to Multiply all numbers in the list.
''' def multList(arr):
    result=1
    for n in arr:
        result*=n
    return result
def main():
    Inp = input("Enter an array (space-separated numbers): ").split()
    Inp = [float(x) for x in Inp]
    result = multList(Inp)
    print(f"The product of the numbers is: {result}")
if __name__ == "__main__":
    main()
#------------------------ '''
# Write a Python program to find the odd numbers in a list.
''' def seperateEvenList(arr):
    evenList=[]
    evenList=[i for i in arr if i%2==1]
    return evenList
def main():
    arr=input("Enter a list with space sperated numbers: ").split()
    arr=[float(x) for x in arr]
    print(f"The even numbers in the list are: {seperateEvenList(arr)}")
    return seperateEvenList(arr)
if __name__ == "__main__":
    main() '''
#------------------------
''' #A practical example for understanding lists.
arr=[1,2,3,4,5,6,7,8,9,20]
arrCopy=arr[:]
# arrCopyReverse=arrCopy.reverse()
arrCopyLast4=arrCopy[:4]
arrCopyFirst4=arrCopy[4:]
arrCopyLast4R=arrCopy[:-4]
arrCopyFirst4R=arrCopy[-4:]
print(f"Original array is: {arr}")
print(f"Copied array is: {arrCopy}")
# print(f"Reversed elements are: {arrCopyReverse}")
print(f"Last 4 elements are: {arrCopyLast4}") 
print(f"First 4 elements are: {arrCopyFirst4}")
print(f"Last 4 elements are: {arrCopyLast4R}")
print(f"First 4 elements are: {arrCopyFirst4R}")
 '''
