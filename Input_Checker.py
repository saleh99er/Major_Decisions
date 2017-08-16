#Function Descritption:
  #This Function is meant to be place into any function that uses a raw_input.
  #This Function check that there is no numbers within the input and that it is a string.

def Input_Checker(INPUT):
  #We start by assuming that there is no numbers witin the string nd that the input is a string.
  noNumbers=True
  #THE "INPUT" VARIABLE IS MEANT TO CHNAGE DEPENDIN OF THE FUNCTION THAT IT'S BEING APPLIED TO
  if type(INPUT)==str and len(INPUT)>0:
    if "0" in INPUT or "1" in INPUT or "2" in INPUT or "3" in INPUT or "4" in INPUT or "5" in INPUT or "6" in INPUT or "7" in INPUT or "8" in INPUT or "9" in INPUT: 
      noNumbers=False
      return noNumbers
    else:
      return noNumbers
  else:
    noNumbers=False
    return noNumbers