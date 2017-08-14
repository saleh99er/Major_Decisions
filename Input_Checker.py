#Script Descritption:
  #This script is meant to be place into any function that uses a raw_input.
  #This script check that there is no numbers withi the input and that it is a string.
#We start by assuming that there is no numbers witin the string nd that the input is a string.
noNumbers=True

#THE "INPUT" VARIABLE IS MEANT TO CHNAGE DEPENDIN OF THE FUNCTION THAT IT'S BEING APPLIED TO

#Nested for loop checks if the is a number(string) in any of the indexes
for i in range(len(INPUT)):
  for j in range(10):
    if INPUT[i]==str(j):
      noNumbers = False

if noNumbers == False:
  print "There are no majors that exist that have numbers in them. Please enter a valid major."
# The final cehck, if the input passes this, a value for the input is returned. 
if noNumbers==True and type(INPUT)==str and len(INPUT)>0:
  validInput=len(INPUT) 