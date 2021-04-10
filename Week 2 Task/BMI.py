# BMI labwork 2.2 week 2 
# Author  Catherine Leddy
# Ref https://www.w3resource.com/python-exercises/python-basic-exercise-66.php
# Ref https://stackoverflow.com/questions/20405610/bmi-calculator-in-python/20405792
# Ref https://www.includehelp.com/python/bmi-body-mass-index-calculator.aspx




name = input ('Hey what is your name?')
print ( 'Hello' + name )

height = float(input('Hey{} what is your height in cm?:' .format (name)))
weight = float(input('Hey{} name what is your weight in kg? :' .format(name)))
Newheight = ((height/100)**2)
BMI= float( weight / Newheight)
print("Your BMI is {}".format (BMI))








