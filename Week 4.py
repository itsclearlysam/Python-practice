VARIABLES AND EXPRESSIONS
------------------------->


good vs bad bits of coding examples:


BAD: 
x1q3z9ocd = 35.0 
x1q3z9afd = 12.50
x1q3p9ocd = x1q3z9ocd + x1q3z9afd           (not friendly or readible for humans, good for python)
print (x1q3p9afd) 

GOOD:
a = 35.0 
b = 12.50                              (friendly for humans to read and also for python)
c = a * b                                 (not numotic, no variable names set)
print(c)


 Numotic example:
 hours = 35.0 
 rate = 12.50
 pay = hours * rate
 print(pay)
 output: 437.5


--------------------------------------------------------------------------
 Numeric expressions:
     +   addition
     -   subtraction
     *   multiplication
     /   division
     **  power
     %   remainder



     When we string operators, Python must know which one to do first. 
     This is called "operator precedence"
 
   
     OPERATOR PRECEDENCE RULES:

     Highest percedence rule to lower precedence rule
     - ( ) are always respected
     - Exponentiation (raise to a power) 
     - Multiplication, Division, and Remainder 
     - Addition and Subtraction
     - Left to right 



     PARENTHESIS
     POWER
     MULTIPLICATION
     ADDITION
     LEFT TO RIGHT



Example: 

x = 1 + (((2 ** 3)/ 4) * 5)                1 + 2 ** 3 / 4 * 5 
print(x)                                       ______
11.0                                       1 + 8 / 4 * 5 
                                               ------
                                              1 + 2 * 5
                                               ------
                                               1 + 10
                                                 11

Numbers have two main types:

- intergers are whole numbers: -2, 0, 1, 100, 2349
- floating point numbers have decimal parts: -2.5, 0.0, 98.6, 14.0

--------------------------------------------------------------------------
Comments in python:
- anything after # is ignored by python
- document who wrote the code or other info
- turn off a line of code - perhaps temporarily 
- describe whats going to happen in a sequence of code 



Example:

# Get the name of the file and open it
name = input('Enter file') 
handle = open(name, 'r') 

# Count word requency 
counts = dict()
for line in handle: 
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

# Find the most common word
bigcount = None
bigword = None
for word,count in counts.items() : 
    if bigcount is None or count > bigcount:
       bigword = word
       bigcount = count

# All done
print(bigword, bigcount) 
        

--------------------------------------------------------------------------


Converting user input 

- if we want to read a number from the user, we must convert it from a string to a number using a type conversion function 

# Convert elevator floors
inp = input('Europe floor?')
usd = int(inp) + 1
print('US floor'. usf)

Europe floor? 0 
US floor 1 


------------------------

2.2   Write a program that uses input to prompt a user for their name and then welcomes them. Note that input will pop up a dialog box. 
      Enter Sarah in the pop-up box when you are prompted so your output will match the desired output.
      
      
      code-
      
      
      # The code below almost works
      
      *******************
      

        name = input("Enter your name")

        print ("Hello",name)
        
        ***********************
        
   Desired Output
Hello Sarah

your output
Hello Sarah
    
----------------------------------

2.3  
Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
You should use input to read a string and float() to convert the string to a number. Do not worry about error checking or bad user data.



code----
********************


hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
pay= hrs*rate
print ("Pay:",pay)


************************


Desired Output
Pay: 96.25

your output
Pay: 96.25






     
