pass #appJar will evetually be getting their input and then using these functions to calculate values.
pass #so raw_input will be removed at some point.
pass #Do research into the concept of "pass". Never though I had to ever write that. 

from random import randint

def intendedMajorQ():
  #first question: What is their intended major then calculates with this
  # and moves on to next one if answer is valid otherwise requires a new response
  # Info extracted from this, length of the string they gave ranging from 3 to 16
  
  #noNumber s is used to check if the input is valid
  # validInput and Back_up_value are used for the condition of the wile loop and are the return values. 
  noNumbers = True
  validInput=0
  Back_up_value=0
  
  # A while loop that keeps stating that an input is false if the user does not input a valid input. This will be added in the main.py.
  #The while statment will look something like:
    #while validInput=0 and Back-up-value=0
    
  #The first question asks the user for their intended major, and if the input is valid, stores the length of the string as a value"""
  major= raw_input("What is your intended major? ")
  
  #for-loop here that will check for any number(string) within the major.
  for i in range(len(major)):
    for j in range(10):
        if major[i]==str(j):
          noNumbers=False
  if noNumbers==False:
    print "There are no majors that exist that have numbers in them. Please enter a valid major."
    
  #Another for-loop that checks if any number(int) is within the major.
  if NoNumbers==True: 
    for i in range(len(major)):
      for j in range(10):
         if major[i]==j:
            noNumbers=False
  if noNumbers==False:
    print "There are no majors that exist that have numbers in them. Please enter a valid major."
    
  # The final cehck, if the input passes this, a value for the input is returned. 
  if noNumbers==True and type(major)==str and len(major)>0:
    validInput=len(major)
  else:
    print "This is not a valid major. Please enter a valid one."
  # A back up if-statement in the case a value that is not expected is generated. 
  if validInput < 3 or validInput> 16:
    Back_up_value=randint(3,16) #randint includes values 3 and 16 but your conditional is exclusive, choose one or the other please
                                #Unsure of what Saleh meant: Do reseacrh into randint. 
    return Back_up_value
  else:
    return validInput