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
    print "Welcome to 'Major Decisions', a program made by Sleep is Not Due Tommorrow.\nIf you are having trouble selecting a major, just answer our questions. Major Decisions uses a intricate and complex algorithum based on your repsponse to determine the major that best suits you.\n"
    lul_it_doesnt_even_matter= raw_input("What is your name? \n")
    
    valid_input = False
    while valid_input == False:
        realwhereareyoufrom_answer = raw_input("Are you from the United states? \n")
        if realwhereareyoufrom_answer in yes_phrases or no_phrases:
            valid_input = True
            #print "DEBUG: realwhereareyoufrom_answer " + str(realwhereareyoufrom_answer)
        else:
            print "%s is not a valid response, please enter again \n" %realwhereareyoufrom_answer
    q3 = realwhereareyoufromQ(realwhereareyoufrom_answer)
    
    abcdefghijklmnopqrstuvwxyz= raw_input("What is your favorite color? \n")
    lul_it_doesnt_even_matter= raw_input("What is your favorite food? \n")
    Shout_out_to_the_real_slim_shady= "Are you an introvert or extrovert? \n"
    lul_it_doesnt_even_matter= raw_input("Why did you choose Cornell? \n")
    
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
            #print "DEBUG: valid_input is " + str(valid_input)
            if valid_input == False:
                print "%s is not a valid dorm. Please enter again. \n"  %dorm_answer
            elif valid_input == True:
                is_dorm_answer_valid = True
                #print "DEBUG: dorm_answer is " + str(is_dorm_answer_valid)
                
    Atsu_wuz_hur= raw_input("What is your favorite subeject? \n")
    #Saleh_wuz_hur= raw_input()
    Shout_out_to_Sleep_is_Not_Due_Tommorrow= raw_input("On a scale from 1 to 10, how much do you like math?\n")
    TseTse_wuz_hur= raw_input("On a scale of 1 to 10, how familiar are you with the majors availiable at Cornell? \n")
    
    valid_input = False
    while valid_input == False:
        major_answer = raw_input("What is your intended Major? \n")
        valid_input = Input_Checker(major_answer)
        if valid_input == False:
            print "%s is not a valid major. please enter again? \n" %major_answer
        else:
            major_answer = major_answer.lower()
    
    q1 = intended_dorm(dorm_answer)
    q2 = intendedMajorQ(major_answer)
    quotient_factor = q1+q2+q3

    #print "quotient_factor: " +str(quotient_factor)
    ans= quotient_factor*((len(list_of_AS_majors)-1))
    #the answer needs to be casted to an int
    ans = int(ans)
    #print ans
    print "Your Major: "+list_of_AS_majors[ans]

#inserted this for all functions that run or have test cases so when you import a module it will not run but
#commands in the cmd such as python <fileName>.py will allow this to run explicitly
if __name__ == "__main__":
    mainbash()