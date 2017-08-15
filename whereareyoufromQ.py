def whereareyoufromQ():
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