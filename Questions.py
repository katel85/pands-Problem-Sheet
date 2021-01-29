# ask for name and set up for reading out name in response to prompt
# Kate Leddy

name= input('what is your name') 
print ('hello ' + name)

#first pose the question this is the input 
# In order to save the answer to the question it must be saved as "name " = input

age= int(input('Hey what is your age?:'))
newNumber = age - 5
print ( ' your age is {} wow you are so young you could pass for {} ' .format (age, newNumber))

# want to add an additional age but I get newage= str (age - 5) incorrect formatting in code 
# fix: needed to put int before the input
# prob File ".\readkate.py", line 11
# fix I needed to close the brackets at the end of line 11!!!

place= input( 'where do you like to go on holidays')
print (' {} is an amazing place to go on holidays ' .format (place))

