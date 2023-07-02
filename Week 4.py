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
