# Write a program that asks the user to input any positive integer and outputs the successive values of the 
# following calculation.At each step calculate the next value by taking the current value and, if it is even, 
# divide it by two, but if it is odd, multiply it by three and add one.Have the program end if the current value is one.
# Author Catherine Leddy

number=int(input('Enter a positive integer number:'))

def collatz (number): # number is the parameter
    while number !=1:# this loop will ensure code will run until number reaches 1
        if number % 2 == 0:  # this division will be used when number is even
            number= number//2
            print(number)
        else:
           number=  3 * number + 1
           print(number)    

collatz(number)

# in the first line of code the number is defined by asking the user to input a positive integer number.
#Collatz is then defined the number is used in this definition. The number is now passed into the function.
# The next line of code (while loop) is a indefinate iteration as long as the number is not 1 
# The if statement will run as long as the statement is true. Statement here is if the number is even (%2==0)
# then the number divide and floor the number (// floor)
# if this statement is not true the else statement will take the number and multiple by 3 and add 1.
# the def key will create a function and call the function collatz and pass a (number) into the function
# the double slash // means divide and then floor the number

# ref https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# ref https://www.youtube.com/watch?v=lAp_5qTdOhM
# ref: https://m-nayoumi.medium.com/generating-a-collatz-sequence-using-a-python-program-56c8fbc318c9
# ref:https://www.educative.io/edpresso/how-to-generate-the-collatz-sequence-in-python





