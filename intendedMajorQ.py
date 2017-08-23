from random import uniform
from Input_Checker import Input_Checker 
def intendedMajorQ():
  #The function "Input_Checker" checks if there is a number(string) wihtin the input.
  major=raw_input("What is your intended Major? \n")
  #WHY WHILE LOOPS WHY 
  noNumbers=Input_Checker(major)
  if noNumbers==True:
    #A value between 0 and .6 will be generated
    validInput=len(major)
    for i in range(4):
      print "Calculating Value...\n" 
  else:
    print "This is not a valid major. Please enter a valid one."
    valid_major=raw_input("What is your intended Major? \n")
    validInput = intendedMajorQ(valid_major)
    return validInput
  if validInput < 3:
    #This generates a value between 0 and .3
    output = uniform(.0,.1)
    print "Value Generated: " + str(output)
    return output
  #The length of the shortest known major is 3 and the length of the largest known major is 28
  elif validInput >=3 and validInput <= 28:
   #Generates a value between 0.0 and 
    output = uniform(.0,.4)
    print "Value Generated: " + str(output)
    return output
  else:
    output= uniform(.2,.3)
    return output

if __name__ == "__main__":
  intendedMajorQ()