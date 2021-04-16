# Write a program that reads in a text file and outputs the number of e's it contains.
# Author Catherine Leddy

import sys # this will let me read the file in as an argument.(Andrew Feedback)

#print(sys.argv) check to see what files are on the system

#filename=sys.argv[1] # define the modydick.txt as filename. es.py = 0 mpbydick.txt =1 


#with open (filename) as f:
    #print (f.read())- check that the file will read in correctly
def NumberE(filename, letter):
    filename=sys.argv[1] 
    with open(filename) as f:
        text = f.read()
        count = 0
     
    for char in text:
          
        if char == letter:
            count += 1
      
    return count
    
  
print(NumberE ('filename', 'e'))
