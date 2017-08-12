
#first question: What is their intended major then calculates with this
# and moves on to next one if answer is valid otherwise requires a new response
# Info extracted from this, length of the string they gave ranging from 3 to 16
from random import randint 
def intendedMajorQ():
  """The first question asks the user for their intended major, and if the inptu is valid, stores the length of the string as a value"""
  major= raw_input("What is your intended major? ")
  if type(major)==str and len(major)>0:
    #add for loop here that will check for any number string within the major. Else statement will be print "This is not a valid major. Please enter a valid one."
    value_1=len(major)
  else:
    print "This is not a valid major. Please enter a valid one."
    intendedMajorQ()
  if value_1 < 3 or value_1 > 16:
    Back_up_value=random.randint(3,16)
    return Back_up_value
  else:
    return value_1