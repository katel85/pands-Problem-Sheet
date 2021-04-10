pip Install markdown
pip Install Pygments


# Pands-Problem-Sheet-G00048625


Week 2 Lab Task- Write a program that calculates somebody's Body Mass Index (BMI)
The inputs are the person's height in centimetres and weight in kilograms.
The output  is their weight divided by their height in metres squared.

BMI labwork Week 2  

Author  Catherine Leddy

Code for Task:

name = input ('Hey what is your name')

print ( 'Hello' + name )

height = float(input('Hey{} what is your height in cm :' .format (name)))

weight = float(input('Hey{} name what is your weight in kg :' .format(name)))

Newheight = ((height/100)**2)

BMI= float( weight / Newheight)

print("Your BMI is {}".format (BMI))

Explanation:


1. First step was to research and look at sample code in the below references.
2. I started with code asking the user for their name. I used input function here along with the question in the parathesis with inverted commas to phrase the question.
3. This code when run will great the user and ask for their name
4. Next I defined the variables height and weight- initially I had used int(no decimal point) but this threw errors when running code and I changed this to float (floating point number has a floating number or decimal point). I used the curly braces {} to insert the names for these questions and used .format at the end of the question to insert user name in all the questions here.
5. For the BMI calculation I had to create a new variable called Newheight because height was given in cm and this had to be converted to m2 using ((height/100)**2) formula.
6. The BMI formula was then written in the code as BMI= float( weight / Newheight)
7. Finally the output is printed as the persons BMI using again the curly braces {} to read in the BMI variable.


References: 

https://www.w3resource.com/python-exercises/python-basic-exercise-66.php

https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792

https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx
