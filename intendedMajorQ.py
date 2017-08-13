pass #appJar will evetually be getting their input and then using these functions to calculate values.
pass #so raw_input will be removed at some point.
pass #Do research into the concept of "pass". Never though I had to ever write that. 

from random import randint

def intendedMajorQ():
  """The first question asks the user for their intended major, and if the input is valid, stores the length of the string as a value

  first question: What is their intended major then calculates with this
  and moves on to next one if answer is valid otherwise requires a new response
  Info extracted from this, length of the string they gave ranging from 3 to 16
  """
  major= raw_input("What is your intended major? ")
  
  noNumbers = True
  Left all my changes like this so you guys can see it
  #add for-loop here that will check for any number(string) within the major. 
  #If there isn't, then noNumbers will reamain true.
  #Else statement will be "print "This is not a valid major. Please enter a valid one."" and NoNumbers=False
  #Use a nested for-loop.
    THERE IS NO NEED FOR THIS LOOP, a while loop is needed to force the user to reenter the data if invalid #The first one will be for the index(ranging from 0 to (len(major-1)))
    use range and for loop to get these values then cast to a string and then track the string with:#The second will be for the numbers(string)(Ranging from 0 to 9)
    substring in string if this boolean expression is true, then set noNumbers = False.
    #noNumbers=False 

  THIS LOOP IS UNNECCESSARY
  #Make another for-loop that checks if any number(int) is within the major.
  #If a number(int) is found, then noNumbers=False
  #Else Statment will be noNumbers will remain True and print "This is not a valid major. Please enter a valid one."
  #IF YOU USE a for loop, in order to go through integers 0 to n-1 in ascending order you can do:
  #for num in range(10): goes through numbers 0 - 9
  

  if noNumbers==True and type(major)==str and len(major)>0:
    value_1=len(major)
  else:
    print "This is not a valid major. Please enter a valid one."
    # Please use a while loop to ask for a new major and check if that major is valid.


  if value_1 < 3 or value_1 > 16:
    Back_up_value=randint(3,16) randint will select a random number between 3 and 16 inclusively but in line 42 you are exclusive (not including the values 3 and 16). To make the numbers selected fair please make the comparison statements use <= >= so those numbers are included as okay or change the random range to 4 to 15 (which is what I least prefer since art is a major and its 3 letters long)
    return Back_up_value
  else:
    return value_1