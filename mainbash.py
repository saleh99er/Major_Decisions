from intended_dorm import intended_dorm
from intendedMajorQ import intendedMajorQ
from realwhereareyoufromQ import realwhereareyoufromQ
def mainbash():
  list_of_AS_majors=["Economics","Philosophy","Chemistry & Chemical Biology",
                   "German Studies","Africana Studies","History","Linguistics",
                   "Astronomy","American Studies","Performing & Media Arts","Music",
                   "Psychology","French","Feminist, Gender & Sexuality Studies",
                   "Spanish","Computer Science","Near Eastern Studies",
                   "Religious Studies","English","College Scholar",
                   "Comparative Literature","Mathematics","Statistical Science",
                   "Biological Sciences","Physics","Government","Classics",
                   "Science & Technology Studies","Independent Major",
                   "China & Asia-Pacific Studies","Anthropology",
                   "Science of Earth Systems","Information Science",
                   "Archaeology","Sociology","Italian","Biology & Society",
                   "Asian Studies","History of Art"]
  # is_US=raw_input("Are you from the United states?")
  # State= raw_input("Is applicable, what state are you from")
  # Country=raw_input("What country are you from")
  # major=raw_input("What is you intended major")
  # dorm= raw_input("Where will you be living?")
  q1 = intended_dorm()
  q2 = intendedMajorQ()
  q3 = realwhereareyoufromQ()
  ans = int((q1+q2+q3)*(len(list_of_AS_majors)-1))
  print list_of_AS_majors[ans]
value=mainbash()