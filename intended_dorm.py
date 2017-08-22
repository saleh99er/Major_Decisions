from random import uniform
from random import random
from Input_Checker import Input_Checker 
def intended_dorm():
  a = ['mews','mews hall']
  b = ['townhouse','townhouse community']
  c = ['balch','balch hall']
  d = ['clara dickson','clara dickson hall']
  e = ['bauer','court-kay-bauer','court kay bauer','court-kay-bauer hall','court kay bauer hall']
  f = ['high rise','high rise','high rise #5','high rise #5']
  g = ['jameson','jameson hall']
  h = ['low rise','low rise','low-rise #6','low-rise #6','low rise #6','low rise #6','low-rise #6','low-rise #6']
  i = ['low-rise #7','low-rise #7','low rise #7','low rise #7','low-rise #7','low-rise #7']
  j = ['mary donlon','mary donlon hall','mary','mary hall','donlon','donolon hall', 'egg']
  k = ['akwe:kon','akwekon','akwe kon','akwe-kon']
  l = ['ecology house','ecology-house','the ecology-house','the ecology house']
  m = ['holland international living center','the holland international living center', 'hilc', 'the hilc']
  n = ['just about music','jam']
  o = ['latino living center','the latino living center','llc']
  p = ['multicultural living learning unit','multicultural living learning unit','the multicultural living learning unit','mcllu']
  q = ['risley residential college','the risley residential college','risley']
  r = ['ujamaa residential college','uj','ujamaa','the ujamaa residential college']
  s = ['language house','the language house','lh']
  master_dorm_list=[a,b,c,d,e,g,h,i,j,k,l,m,n,o,p,q,r,s]
  
  # This while loops keeps running until the user gives a valid input.
  valid_input = False
  while valid_input == False:
    dorm = raw_input("Where will you be living? \n")
    valid_input = Input_Checker(dorm)
    if valid_input==False:
       print "%s is not a valid dorm. Please enter again. \n " % dorm 
    else: dorm = dorm.lower()
    is_dorm_name_in_list=False
  while is_dorm_name_in_list==False: 
    for dorm_building in master_dorm_list:
      for dorm in dorm_building:
        if dorm in dorm_building:
          is_dorm_name_in_list=True
    if is_dorm_name_in_list==False:
      print "This is not a valid dorm name. Please enter one."
  # for i in range(4):
  #   print "Calculating Value...\n"
  # The bounds of psuedo-randomness are 0 and .1.
  # The for-loops checks for whether the user's input matches any of the dorms names.
  # As the check moves to the next 'dorm_building', the bounds of randomness are shifted by the variable "increment"
    #Ex: when dorm_building = a, the bound of randomness are 0 and .1
    # when dorm_building = b, the bounds of randomness are the [value of increment] and [.1 + value of increment]
  lower_bound = 0
  higher_bound = .1
  increment = float(.2/(len(master_dorm_list)-1))
  for dorm_building in master_dorm_list:
    for dorm_name in dorm_building:
      if dorm == dorm_name:
        ans=uniform(lower_bound,higher_bound)
        print "Value Generated: " + str(ans)
        return ans
      else:
        lower_bound =  lower_bound + increment
        higher_bound = higher_bound + increment
intended_dorm()