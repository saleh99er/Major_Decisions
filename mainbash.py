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
  q1 = intended_dorm()
  q2 = intendedMajorQ()
  q3 = realwhereareyoufromQ()
  ans = int((q1+q2+q3)*(len(list_of_AS_majors)-1))
  print list_of_AS_majors[ans]
  mainbash()