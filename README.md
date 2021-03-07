# pands-Problem-Sheet
Week 2 lab

BMI labwork week 2 

Author  Catherine Leddy
Ref https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
Ref https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792
Ref https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx

name = input ('hey what is your name')
print ( 'Hello' + name )
height = float(input('Hey{} what is your height in cm :' .format (name)))
weight = float(input('Hey{} name what is your weight in kg :' .format(name)))
Newheight = ((height/100)**2)
BMI= float( weight / Newheight)
print("Your BMI is {}".format (BMI))


# need to put in a way so that we can put in a decimal point with the kg. Intially used 
# int but because there is a decimal point I will use float

#initially my BMI was coming out at 55 because I had the height as an int. My answer was going to be with decimal points 
# so this also had to be changed to float along with the weight
