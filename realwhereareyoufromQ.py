from random import uniform
def realwhereareyoufromQ(is_US,State,Country):
  if is_US=="Y" or is_US=="Yes" or is_US=="y" or is_US=="yes" or is_US=="YES":
    noNumbers=Input_Checker(State)
    counter=0
    if noNumbers==False:
      print "%s not a valid state. Please enter a valid one " % State
      print " \n "
      new_state= raw_input("What state are you from? ")
      retval=realwhereareyoufrom("Y",new_state, USA)
      return retval
    else:
      for i in len(State):
        if state[i]=="a":
          counter=counter+1
          if counter==1:
            return uniform(.0,.15)
          elif counter==2:
            return uniform(.15,.25)
          elif counter==3:
            return uniform(.0,.3)
          elif couner==4:
            return uniform(.25,.3)
          else:
            return uniform(.0,.3)
  if is_US=="N" or is_US=="Yes" or is_US=="n" or is_US=="no" or is_US=="NO":
    noNumbers=Input_Checker(Country)
    counter=0
    if noNumbers==False:
      print "%s not a valid country. Please enter a valid one " % Country
      print "\n "
      new_Country= raw_input("What state are you from? ")
      retval=realwhereareyoufrom("N","N/A", new_Country)
      return retval
    else:
      for i in len(Country):
        if Country[i]=="a":
          counter=counter+1
          if counter==1:
            return uniform(.0,.15)
          elif counter==2:
            return uniform(.15,.25)
          elif counter==3:
            return uniform(.0,.3)
          elif couner==4:
            return uniform(.25,.3)
          else:
            return uniform(.0,.3)