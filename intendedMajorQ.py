#PLEASE MOVE THE DESCRIPTION BELOW IN THE intendedMajorQ function's specification, in python it can be multiline. pass is like a temp placeholder thing, please delete pass once changes are made
pass    #first question: What is their intended major then calculates with this
pass    # and moves on to next one if answer is valid otherwise requires a new response
pass    # Info extracted from this, length of the string they gave ranging from 3 to 16

#ALSO, please do not name this file after one question we're implementing, it would be a pain to import all these files so I think it's better if we keep all the questions in one file (preferably this one) but we can cross that bridge later once we have multiple questions working

#LASTLY, in appJar, we will be getting their input and then using these functions to calculate values, so for now they're fine but we will stop using raw_input eventually and just use those function's parameters

from random import randint

def intendedMajorQ():
  """The first question asks the user for their intended major, and if the inptu is valid, stores the length of the string as a value"""
  major= raw_input("What is your intended major? ")

  noNumbers = True
  #do it outside thee if statement otherwise it will get the length of it and the user will not know the major is invalid
  #add for loop here that will check for any number string within the major. Else statement will be print "This is not a valid major. Please enter a valid one."


  #put noNumbers in the conditional, in between these comments I recommend you write the code to see if a number is in a string
  #Hint IF YOU USE a for loop, in order to go through integers 0 to n-1 in ascending order you can do:
  #for num in range(10): goes through numbers 0 - 9
  if type(major)==str and len(major)>0:
    value_1=len(major)
  else:
    print "This is not a valid major. Please enter a valid one."
    intendedMajorQ() #bad idea to try to apply recursion here especially since the function is formatted wierd and there is no memory of it's recursive children here, please use a while loop to ask for a new major and check if that major is valid.


  if value_1 < 3 or value_1 > 16:
    Back_up_value=random.randint(3,16) #randint includes values 3 and 16 but your conditional is exclusive, choose one or the other please
                                      #also when you do a from import, the random functions and variables are defined in your local space so
                                      #either do a regular import and continue using dot notation or remove "random." from line 25
    return Back_up_value
  else:
    return value_1