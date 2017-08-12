
#first question: What is their intended major then calculates with this
# and moves on to next one if answer is valid otherwise requires a new response
# Info extracted from this, length of the string they gave ranging from 3 to 16

major= raw_input("What is your intended major? ")
def intendedMajorQ(major):
  """The first question asks the user for their intended major, and if the inptu is valid, stores the length of the string as a value"""
  if len(major)>0 and major.isalpha():
    value_1=len(major)
  else:
    print "This is not a valid major. Please enter a valid one"
    intendedMajorQ(major)
  if value_1 < 3 or value_1 > 16:
        random.randint(3,16)
Value_1=intendedMajorQ(major)