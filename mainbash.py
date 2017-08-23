from intended_dorm import intended_dorm
from intendedMajorQ import intendedMajorQ
from realwhereareyoufromQ import realwhereareyoufromQ
from list_of_AS_majors import list_of_AS_majors #imported this so the list that was here is no longer needed (I removed it)
from Input_Checker import Input_Checker #imported this since we need it in mainbash to check user inputs
#you can from import variables too!
def mainbash():
    valid_input = False
    while valid_input == False:
        dorm_answer = raw_input("Where will you be living? \n")
        valid_input = Input_Checker(dorm)
        #print "DEBUG: valid_input is " + str(valid_input)
        PLEASE CHANGE ALL PRINT STATEMENTS TO STATE DEBUG AND WHAT ITS SUPPOSE TO OUTPUT AND THEN CONCATENATE IT CAREFULLY
        IF THE VARIABLE YOU ARE PRINTING IS NOT A STRING, YOU NEED TO CAST IT. AND EXAMPLE OF THIS IS ABOVE.
    if valid_input==False:
        print "%s is not a valid dorm. Please enter again. \n "
    else:
        dorm_answer = dorm_answer.lower()

    q1 = intended_dorm(dorm_answer)
    q2 = intendedMajorQ()
    q3 = realwhereareyoufromQ()
    quotient_factor = q1+q2+q3

    print "quotient_factor: " +str(quotient_factor)
    ans= quotient_factor*((len(list_of_AS_majors)-1))
    #the answer needs to be casted to an int
    ans = int(ans)
    print ans
    print list_of_AS_majors[ans]
    GUYS INTENT PROPERLY THIS TIME -_- (USE TAB)

#inserted this for all functions that run or have test cases so when you import a module it will not run but
#commands in the cmd such as python <fileName>.py will allow this to run explicitly.
if __name__ == "__main__":
    mainbash()