pip Install markdown
pip Install Pygments


# Pands-Problem-Sheet-G00048625


# Week 2 Task

_Write a program that calculates somebody's Body Mass Index (BMI)
The inputs are the person's height in centimetres and weight in kilograms.
The output  is their weight divided by their height in metres squared._

_Author  Catherine Leddy_

Code for Task:

name = input ('Hey what is your name')

print ( 'Hello' + name )

height = float(input('Hey{} what is your height in cm :' .format (name)))

weight = float(input('Hey{} name what is your weight in kg :' .format(name)))

Newheight = ((height/100)**2)

BMI= float( weight / Newheight)

print("Your BMI is {}".format (BMI))

Explanation:


- First step was to research and look at sample code in the below references.
- I started with code asking the user for their name. I used input function here along with the question in the parathesis with inverted commas to phrase the question.
- This code when run will great the user and ask for their name
- Next I defined the variables height and weight- initially I had used int(no decimal point) but this threw errors when running code and I changed this to float (floating point number has a floating number or decimal point). I used the curly braces {} to insert the names for these questions and used .format at the end of the question to insert user name in all the questions here.
- For the BMI calculation I had to create a new variable called Newheight because height was given in cm and this had to be converted to m2 using ((height/100)**2) formula.
- The BMI formula was then written in the code as BMI= float( weight / Newheight)
- Finally the output is printed as the persons BMI using again the curly braces to read in the BMI variable.


References: 

<https://www.w3resource.com/python-exercises/python-basic-exercise-66.php>

<https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792>

<https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx>

<https://www.youtube.com/watch?v=pTCROLZLhDM> Markdown Video


# Week 3 Task

_Write a program that takes asks a user to input a string and outputs every second letter in reverse order_

_Author Catherine Leddy_

Code for Task:

sent = str(input("Please enter a sentence and I will output ever second letter for you in reverse order!"))

sent2 = (sent[::-1])

print (sent2[::2])

print ('Hope you like your new sentence!')

Explanation:

- First task was to  create a string asking the user to input a sentence. This was defined as sent. This input will be variable used for the test code to run on.
- The sent (user input) was then coded to  read backwards with sent2 = (sent[::-1]). This code uses string slicing to reverse print the input sentence. We use indexing here with [::-1] index position 0 would denote the end of the string sentence. Therefore -1 (negative indexing)is used so the first letter is included in the code. The slice statement [::-1] means start at the end of the string and end at position 0.
- Second task was to pick every second letter in the reversed sentence with print (sent2[::2]). Here again the index :2 is used to start the code at the second letter. 

References:

<https://stackoverflow.com/questions/20847205/program-to-extract-every-alternate-letters-from-a-string-in-python>

<https://www.w3schools.com/python/python_howto_reverse_string.asp>

<https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python>

Automatetheboringstuff.com. 2020. Automate The Boring Stuff With Python. [online] Available at: <https://automatetheboringstuff.com/chapter6/>



# Week 04 Task 


_Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation.At each step calculate the next value by taking the current value and, if it is even,divide it by two, but if it is odd, multiply it by three and add one.Have the program end if the current value is one_

_Author Catherine Leddy_

Code for Task:

number=int(input('Enter a positive integer number:\n'))

def collatz (number):

    while number !=1:
        if number % 2 == 0:
            number= number//2
            print(number)
        else:
           number=  3 * number + 1
           print(number)    

collatz(number)

Explanation:

- In the first line of code the number is defined as an int and string is used when asking the user to input a positive integer number.
- Collatz is then defined as a function. The number is now passed into the function. The code must be indented after the def or we will encounter indentation errors. 
- The next  few lines of code will now define what the function of collatz is. The first line of code is the  **while loop** . The while loop will execute a set of statements as long as a condition is true . This states that  the code should execute while the number is not equal to 1 . When the number reaches 1 the code will stop running. This is a indefinate iteration as long as the number is not 1.
- The **if** statement will run as long as the statement is true. Statement here is if the number is even (%2==0). Then the number  will be divided by 2 and will be floored (//2). We use the floor function so the number won't have a decimal point when the code runs.
- If this **if** statement is not true the **else** statement will run and take the number and multiple by 3 and add 1.
- The last step collatz(number) function is  called  and the code will run with the data entered from the initial input of the user.
  
References:

<https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff>

<https://www.youtube.com/watch?v=lAp_5qTdOhM>

<https://m-nayoumi.medium.com/generating-a-collatz-sequence-using-a-python-program-56c8fbc318c9>

<https://www.educative.io/edpresso/how-to-generate-the-collatz-sequence-in-python>

Python Functions Examples: Call, Indentation, Arguments & Return Values <https://www.guru99.com/functions-in-python.html#1>

<https://www.w3schools.com/python/python_while_loops.asp>




# Week 05 Task

_Write a program that outputs whether or not today is a weekday_

_Author: Catherine Leddy_

Code for Task:

import datetime

day= datetime.datetime.today().weekday()


if day<5 :

print("Yes, unfortunately today is a weekday.")

else:

print("It is the weekend, yay!")


Explanation:

- To begin we import a module named datetime to work with dates as date objects.
  
- We then use functions from the datetime module to define what the day is.

- For today's date, we use the datetime.today() function from datetime module

- The python weekday function of class date returns the day number of the week as an integer (automatically defaults to an integer) . It starts from 0 for a Monday and ends at 6 for a Sunday

- Then using the conditional statement **if** and **else** we can write the decision making process so that the code will be able to decide whether today is a weekday or weekend.

- Then  the code will check if the day is less than 5 (interger value that the weekeday function will use) then its a weekday otherwise it is a weekend.

References:

<https://www.w3schools.com/python/python_datetime.asp>

<https://www.dataquest.io/blog/python-datetime-tutorial/>

<https://docs.python.org/3/library/datetime.html>

<https://stackoverflow.com/questions/29384696/how-to-find-current-day-is-weekday-or-weekends-in-python>

<https://www.tutorialsrack.com/articles/324/how-to-find-the-current-day-is-weekday-or-weekends-in-python>

<https://www.xspdf.com/resolution/58438157.html>




