#Write a program that asks the user to input any positive integer and outputs the successive values of the 
# following calculation.At each step calculate the next value by taking the current value and, if it is even, 
# divide it by two, but if it is odd, multiply it by three and add one.Have the program end if the current value is one.
# Author Catherine Leddy
# ref https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff
# ref https://www.youtube.com/watch?v=lAp_5qTdOhM


def collatz (number): # number is the parameter

    if number % 2 == 0:  # this division will be used when number is even
        print(number // 2)
        return number // 2 

    elif number % 2 == 1: # elif is used as the second command when number is odd 
        result = 3 * number + 1 
        print (result)
        return result 

n = input ('Give me a positive integer number :')  
while n!= 1: # create a while loop to keep the loop going until 1 is returned 
    n = collatz (int(n))


# if the number is even then collatz will print number divided by 2. step 1 10/2 is 5 which is the first number the 
# the collatz returns. This number is odd so collatz will then (elif function) multiple this by 3 and add 1. This output
# returns 16. 16 is an even number so the number divided by 2 will now return an 8. Even number again so divides by 2 which
# return a 4 and divided by 2 returns a 2 and divided again returns a 1.
# any number you put in this program will eventually return a 1 
# collatz will only work with a positiev integer so you must define this at the beginning with the question
# the def key will create a function and call the function collatz and pass a (number) into the function
# the double slash // means divide and then floor the number







