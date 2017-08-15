def whereareyoufromQ():
  America_or_nah=raw_input("Do you come from a state in America? (Y/N)")
  if America_or_nah=="Y" or America_or_nah=="Yes" or America_or_nah=="y":
    state= raw_input("What state are you from? ")
    noNumbers=True
    for i in range(len(state)):
      for j in range(10):
        if state[i]==str(j):
          noNumbers = False
        
    if noNumbers == False:
      print "%s not a valid State. Please enter a valid one " % state
      output=whereareyoufromQ()
      return output
    #I'm thinking I should do a list of each state and thier abbriavtions as well to have another check. What do you think?
    #The output  values 3 qnd 5 are just for testing, no other reason why I selected it. 
    if noNumbers==True and type(INPUT)==str and len(INPUT)>0:
    # Might hve to change the letter tho becuase like Atsutse said, "a" is to common. have the output value equal to the number of a in a string.
      for i in range(len(state)):
       if state[i]=="a":
        output=3
        return output 
      else:
        output=5
        return output
  #The output value is just for the sake of testing
  elif America_or_nah=="N" or America_or_nah=="No" or America_or_nah=="n":
    country_of_origin= raw_input("Where are you from?")
    noNumbers=True
    for i in range(len(country_of_origin)):
      for j in range(10):
        if state[i]==str(j):
          noNumbers = False
        
    if noNumbers == False:
      print "%s not a valid country. Please enter a valid one " % country_of_origin
      output=whereareyoufromQ()
      return output
    else: 
      output= 4
    return output
  else:
    print "Please answer either \"Yes\" or \"No\""
    output= whereareyoufromQ
    return output