#Function Descritption:
  #This Function is meant to be placed into any function that uses a raw_input.
  #This Function check that there is no numbers within the input and that it is a string.
def Input_Checker(INPUT):
  #We start by assuming that there is no numbers witin the string nd that the input is a string.
  list_of_numbers=["0","1","2","3","4","5","6","7","8","9"]
  noNumbers=True
  for i in range(len(list_of_numbers)):
    if INPUT[i]==list_of_numbers[i] or len(INPUT)<=0:
      noNumbers=False
  return noNumbers