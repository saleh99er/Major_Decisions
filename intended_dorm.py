from random import uniform
from random import random
from Input_Checker import Input_Checker 
def intended_dorm(dorm):
  A = ['mews','mews hall']
  B = ['townhouse','townhouse community']
  C = ['balch','balch hall']
  D = ['clara dickson','clara dickson hall']
  E = ['bauer','court-kay-bauer','court kay bauer','court-kay-bauer hall','court kay bauer hall']
  F = ['high rise','high rise','high rise #5','high rise #5']
  G = ['jameson','jameson hall']
  H = ['low rise','low rise','low-rise #6','low-rise #6','low rise #6','low rise #6','low-rise #6','low-rise #6']
  I = ['low-rise #7','low-rise #7','low rise #7','low rise #7','low-rise #7','low-rise #7']
  J = ['mary donlon','mary donlon hall','mary','mary hall','donlon','donolon hall', 'egg']
  K = ['akwe:kon','akwekon','akwe kon','akwe-kon']
  L = ['ecology house','ecology-house','the ecology-house','the ecology house']
  M = ['holland international living center','the holland international living center', 'hilc', 'the hilc']
  N = ['just about music','jam']
  O = ['latino living center','the latino living center','llc']
  P = ['multicultural living learning unit','multicultural living learning unit','the multicultural living learning unit','mcllu']
  Q = ['risley residential college','the risley residential college','risley']
  R = ['ujamaa residential college','uj','ujamaa','the ujamaa residential college']
  S = ['language house','the language house','lh']
  master_dorm_list=[A,B,C,D,E,G,H,I,J,K,L,M,N,O,P,Q,R,S]
  # This while loops keeps running until the user gives a valid input.

      #is_dorm_name_in_list=False

  # The bounds of psuedo-randomness are 0 and .1.
  # The for-loops checks for whether the user's input matches any of the dorms names.
  # As the check moves to the next 'dorm_building', the bounds of randomness are shifted by the variable "increment"
    #Ex: when dorm_building = A, the bound of randomness are 0 and .1
    # when dorm_building = B, the bounds of randomness are the [value of increment] and [.1 + value of increment]
  lower_bound = 0
  higher_bound = .1
  increment = float(.2/(len(master_dorm_list)-1))
  for dorm_building in master_dorm_list:
    for dorm_name in dorm_building:
      if dorm == dorm_name:
        ans=uniform(lower_bound,higher_bound)
        #print "Value Generated: " + str(ans)
        return ans
      else:
        lower_bound =  lower_bound + increment
        higher_bound = higher_bound + increment

if __name__ == "__main__":
  intended_dorm()