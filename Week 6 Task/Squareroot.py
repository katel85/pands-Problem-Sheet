# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root
# Author Catherine Leddy

# Ref: https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N.
# Ref: https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
    # Newtons definition for a square root 
    # Let N be any number then the square root of N can be given by the formula:
    # root = 0.5 * (X + (N / X)) where X is any guess which can be assumed to be N or 1.

def newton(x): # here we are calling the function newton and passing in the argument (x)
   tolerance = 0.000001 #this is the degree of accuracy you want 
   estimate = 3.0 # this is the estimated sqrt (the guessed sqrt). This number can be anything you want.
   while True:
        estimate = (estimate + x / estimate) / 2 #newtons equation for a guessed sqrt
        difference = abs(x - estimate ** 2)      # newtons equation for a quessed sqrt
        if difference <= tolerance: 
            break
   return estimate

def main():
   while True:
       x = input("Enter a positive number or enter/return to quit: ")
       if not x:
           break
       x = float(x)
       x1 =round(newton(x),1)
       print ("The program's estimate of the square root of {} is {}".format(x,x1))
main()





      
         



