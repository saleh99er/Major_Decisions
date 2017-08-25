from intended_dorm import intended_dorm
from intendedMajorQ import intendedMajorQ
from realwhereareyoufromQ import realwhereareyoufromQ
from realwhereareyoufromQ import yes_phrases
from realwhereareyoufromQ import no_phrases
from list_of_AS_majors import list_of_AS_majors #imported this so the list that was here is no longer needed (I removed it)
from Input_Checker import Input_Checker
from dorm_checker import dorm_checker
#imported this since we need it in mainbash to check user inputs
#you can from import variables too!
def mainbash():
    
    valid_input = False
    while valid_input == False :
        dorm_answer = raw_input("Where will you be living? \n")
        valid_input = Input_Checker(dorm_answer)
        #print "DEBUG: valid_input is " + str(valid_input)
        if valid_input==False:
            print "%s is not a valid dorm name. Please enter again. \n"  %dorm_answer
        else:
            dorm_answer = dorm_answer.lower()
            valid_input = dorm_checker(dorm_answer) 
            if valid_input == False:
                print "%s is not a valid dorm. Please enter again. \n"  %dorm_answer
            else:
                is_dorm_answer_valid = True
                print "DEBUG: dorm_answer is " + str(is_dorm_answer_valid)
    valid_input = False
    while valid_input == False:
        major_answer = raw_input("What is your intended Major? \n")
        valid_input = Input_Checker(major_answer)
        if valid_input == False:
            print "%s is not a valid major. please enter again? \n" %major_answer
        else:
            major_answer = major_answer.lower()
    valid_input = False
    while valid_input == False:
        realwhereareyoufrom_answer = raw_input("Are you from the United states? \n")
        if realwhereareyoufrom_answer in yes_phrases or no_phrases:
            valid_input = True
        else:
            print "%s is not a valid response, please enter again \n" %realwhereareyoufrom_answer
    q1 = intended_dorm(dorm_answer)
    q2 = intendedMajorQ(major_answer)
    q3 = realwhereareyoufromQ(realwhereareyoufrom_answer)
    quotient_factor = q1+q2+q3

    #print "quotient_factor: " +str(quotient_factor)
    ans= quotient_factor*((len(list_of_AS_majors)-1))
    #the answer needs to be casted to an int
    ans = int(ans)
    #print ans
    print list_of_AS_majors[ans]

#inserted this for all functions that run or have test cases so when you import a module it will not run but
#commands in the cmd such as python <fileName>.py will allow this to run explicitly
if __name__ == "__main__":
    mainbash()