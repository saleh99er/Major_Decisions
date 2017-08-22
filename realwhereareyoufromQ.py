from random import uniform
from Input_Checker import Input_Checker
def realwhereareyoufromQ():
  America_or_nah=raw_input("Are you from the United states?\n")
  America_or_nah=America_or_nah.strip()
  yes_phrases = ["Y","Yes","y","yes","YES","YAS","AMERICAAAAAA!!!"]
  no_phrases =  ["N","No","n","no","NO","Nah","Nope"]
  is_US=False
  CorrectInput=False
  while CorrectInput== False:
    if America_or_nah in yes_phrases:
      is_US=True
      CorrectInput=True
    elif America_or_nah in no_phrases:
      is_US=False
      CorrectInput=True
    else:
      print "Please answer yes or no"
      America_or_nah=raw_input("Are you from the United states?")
      
  if is_US==True:
    noNumbers=False 
    while noNumbers==False:
      State=raw_input("What state are you from? \n")
      noNumbers=Input_Checker(State)
      if noNumbers==False:
        print "%s not a valid state. Please enter a valid one \n " % State
    for i in range(4):
      print "Calculating Value...\n" 
    counter=0
    for i in range(len(State)):
      if State[i]=="a":
        counter=counter+1
    if counter==1:
      ans=uniform(.0,.15)
      print ans
      return ans 
    elif counter==2:
      ans=uniform(.15,.25)
      print ans
      return ans 
    elif counter==3:
      ans=uniform(.0,.3)
      print ans
      return ans 
    elif couner==4:
      ans=uniform(.25,.3)
      print ans 
      return ans 
    else:
      ans=uniform(.0,.3)
      print ans
      return ans
        
  if is_US==False:
    noNumbers=False
    while noNumbers==False:
      Country=raw_input("What country are you from? \n")
      noNumbers=Input_Checker(Country)
    for i in range(4):
      print "Calculating Value...\n" 
    counter=0
    for i in range(len(Country)):
      if Country[i]=="a":
        counter=counter+1
    if counter==1:
      ans=uniform(.0,.15)
      print ans
      return ans 
    elif counter==2:
      ans=uniform(.15,.25)
      print ans 
      return ans 
    elif counter==3:
      ans=uniform(.0,.3)
      print ans
      return ans 
    elif counter==4:
      ans=uniform(.25,.3)
      print ans
      return ans
    else:
      ans=uniform(.0,.3)
      print ans 
      return 
realwhereareyoufromQ()