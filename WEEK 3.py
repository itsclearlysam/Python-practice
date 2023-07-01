Notes for week 3 :

WRITING PARAGRAPHS IN CODE!!
----------------->
x = 1
print (x)
1
x = x + 1
print (x)
2
exit()  

THIS IS A GOOD TEST TO MAKE SURE THAT YOU HAVE PYTHON CORRECTLY INSTALLED.
----------------->

Elements of Python
- Vocabulary / Words - variables and reserved words (CHAPTER 2)
- Sentence structure - valid syntax patterns (CHAPTER 3-5)
- Story structure - consructing a program for a purpose
----------------->

RESERVED WORDS:
false 
none
true 
and 
as 
assert 
break
class 
if 
def
del 
elif
else
except
return 
for 
from
global
try
import
in
is
lambda
while
not
or
pass
raise
finally
continue
nonlocal
with
yield

---------------->


Sentences or Lines

x = 2 <--- Assignment statement
x = x + 2 <--- Assignment statement
print (x) <--- Print function

Variable   Operator  Constant  Function
  (x)        (=)       (2)     (print)

----------------->

PYTHON SCRIPTS

( .py ) to save python files

Program steps or program flow: 

1. Like a  recipe, a program is a SEQUENCE of steps tp be done in order. 
2. Some steps are CONDITIONAL and may be skipped.
3. Sometimes a step or gorup of steps is to be REPEATED. 

------------------------------------------------------------------------->

SEQUENTIAL STEPS

x = 2                    Program:          Output:
  |                  
print(x)                  x = 2
  |                       print(x)            2
x = x + 2                 x = x + 2
  |                       print(x)            4
print(x)

------------------------------------------------------------------------->
 
CONDITIONAL STEPS

x = 5                           Program:                        Output: 
x = 10   print('Smaller')      x = 5
x > 20   print('Bigger')       if x < 10:
print('Finis')                       print('Smaller')           Smaller
                               if x > 20: 
                                     print('Bigger')       
                               print('Finis')                     Finis

------------------------------------------------------------------------->

REPEATED STEPS

n = 5                          Program:                         Output:
n > 0              
print(n)                       n = 5                               5
n = n - 1                      while n > 0 :                       4
print('Blastoff!')                 print(n)                        3
                                   n = n - 1                       2
                               print('Blastoff!')                  1
                                                               Blastoff!



