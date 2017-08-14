

from random import randint

def intendedMajorQ():
  """The first question asks the user for their intended major, and if the input is valid, stores the length of the string as a value

  first question: What is their intended major then calculates with this
  and moves on to next one if answer is valid otherwise requires a new response
  Info extracted from this, length of the string they gave ranging from 3 to 16

  appJar will evetually be getting their input and then using these functions to calculate values.
  so raw_input will be removed at some point.
  Do research into the concept of "pass". Never though I had to ever write that.
  """
   #The first question asks the user for their intended major, and if the input is valid, stores the length of the string as a value"""
  major= raw_input("What is your intended major? ")
  #noNumber s is used to check if the input is valid
  # validInput and Back_up_value are used for the condition of the wile loop and are the return values. 
  noNumbers = True
       
  for i in range(len(major)):
    for j in range(10):
        if major[i]==str(j):
          noNumbers = False
  if noNumbers == False:
    print "There are no majors that exist that have numbers in them. Please enter a valid major."
    
  # The final cehck, if the input passes this, a value for the input is returned. 
  if noNumbers==True and type(major)==str and len(major)>0:
    validInput=len(major)
    print "DEBUG: this is a valid major, calculating"
  else:
    print "This is not a valid major. Please enter a valid one."
    validInput = intendedMajorQ()
  if validInput <= 3 or validInput >= 16:
    Back_up_value=randint(3,16) #IF your going to have random values between 3 and 16 (inclusive) then you need a condition that states 3 and 16 are valid numbers
    print "DEBUG: major is too small or too big, fabricating new value" + str(Back_up_value)
    return Back_up_value

  else:
    print "DEBUG: returning proper value " + str(validInput)
    return validInput