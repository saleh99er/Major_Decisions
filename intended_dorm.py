from random import random
def intended_dorm():
  valid_input = False
  while valid_input == False:
    dorm = raw_input("Where will you be living?")
    dorm = dorm.lower()
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
    if dorm == a in dorm:
      return random()*.3
      valid_input = True
    elif dorm == b in dorm:
      return random()*.3
      valid_input = True
    elif dorm == c in dorm:
      return random()*.3
      valid_input = True
    elif dorm == d in dorm:
      return random()*.3
      valid_input = True
    elif dorm == e in dorm:
      return random()*.3
      valid_input = True
    elif dorm == f in dorm:
      return random()*.3
      valid_input = True
    elif dorm == g in dorm:
      return random()*.3
      valid_input = True
    elif dorm == h in dorm:
      return random()*.3
      valid_input = True
    elif dorm == i in dorm:
      return random()*.3
      valid_input = True
    elif dorm == j in dorm:
      return random()*.3
      valid_input = True
  else:
    print 'invalid response'
    