def whereareyoufromQ():
  #THE REASON WHY I ADDED COMMENTS FOR WHAT I SHOULD DO INSTEAD OF JUST DOING IT IS BECAUSE I NEED TO MAKE SURE WERE ON THE SAME PAGE ESPECIALLY SINCE YOUR'RE DOING THE GUI
    #NOT YELLING JUST THOUGHT THAT THIS IS IMPORTANT TO READ
  
  #At the get-go, we are going to determine whether the user is from America or not.
  #v I love this variable
  America_or_nah=raw_input("Do you come from a state in America? (Y/N): ")
  #If he/she is from America, then we ask what state they are from and get an return value from that.
  if America_or_nah=="Y" or America_or_nah=="Yes" or America_or_nah=="y":
    state= raw_input("What state are you from? ")
    noNumbers=True
    #Simple check if there is any number within the input
    for i in range(len(state)):
      for j in range(10):
        if state[i]==str(j):
          noNumbers = False
    if noNumbers == False:
      print "%s not a valid State. Please enter a valid one " % state
      print " \n "
      retval=whereareyoufromQ()
      return retval
    #I'm thinking of adding a list cotaining the name of every state and abbriavtions.
    #Then I'm thinking creating check to see whether the input is the same as one of indexes in the list. 
    #What do you think?
    if noNumbers==True and type(state)==str and len(state)>0:
    # Might have to change the letter we check for becuase like Atsutse said, "a" is to common.
    # Maybe we have the return value be equal to the number of a of "a"'s or another letter in the string
      #For example, the greatest amount of "a"s in any state is 3
    #Your opinion?
      for i in range(len(state)):
       if state[i]=="a":
        #The output  values 3 qnd 5 are just for testing, no other reason why I selected it. 
        retval=3
        return retval
      else:
        #Again, I just slected a random return value. Will do math later with Atsutse to figue out what value I should really make them
        #Just want to make sure the function works.
        #This might change if we decide to do the sugeestion I mentioned in the comments above.
        retval=5
        return retval
    else:
      print "%s not a valid State. Please enter a valid one " % state
      print " \n "
      retval=whereareyoufromQ()
      return retval
  #The output value is just for the sake of testing
  elif America_or_nah=="N" or America_or_nah=="No" or America_or_nah=="n":
    country_of_origin= raw_input("Great! An international student! What is your country of origin?")
    noNumbers=True
    for i in range(len(country_of_origin)):
      for j in range(10):
        if state[i]==str(j):
          noNumbers = False
    #Again, should I add a list of countries? I'm probably going to steal it from somewhere on the internet, not make it myself.    
    if noNumbers == False:
      print "%s not a valid country. Please enter a valid one " % country_of_origin
      print " \n "
      retval=whereareyoufromQ()
      return retval
    else:
      #No reason why I picked 4, I'm not a racist and/or islonationist.
      #^^ Not for you Saleh or Atsutse.
      #Just wrote that for the one person who finds a way to be offended by the fact that I was being lazy and didn't want to find a line of code to accoomate that fact. 
      # I'm planning to keep this comment within the code as a disclaimmer that "The Sleep is Not tommorrow Group are not racist and/or have islonationist beliefs."
        #Just in case. 
      # You know what? If we decide to have the return value euqal the number "a"'s or some letter in string, I'll do it for this as well. 
        #Then if the return value is greater than some value (which is to be decided), I'll then return a "Back_up_value" instead
      #What do you think?
      retval= 4
    return retval
  else:
    print "Please answer with either \"Yes\" or \"No\""
    print " \n "
    retval= whereareyoufromQ()
    return retval