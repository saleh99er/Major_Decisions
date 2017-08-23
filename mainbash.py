from intended_dorm import intended_dorm
from intendedMajorQ import intendedMajorQ
from realwhereareyoufromQ import realwhereareyoufromQ
from list_of_AS_majors import list_of_AS_majors #imported this so the list that was here is no longer needed (I removed it)
#you can from import variables too!
def mainbash():
  q1 = intended_dorm()
  q2 = intendedMajorQ()
  q3 = realwhereareyoufromQ()
  quotient_factor = q1+q2+q3gitgit

  print "quotient_factor: " +str(quotient_factor)  
  ans= quotient_factor*((len(list_of_AS_majors)-1))
  print list_of_AS_majors[ans]

#inserted this for all functions that run or have test cases so when you import a module it will not run but
#commands in the cmd such as python <fileName>.py will allow this to run explicitly.
if __name__ == "__main__":
    mainbash()