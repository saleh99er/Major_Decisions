from random import random
def intended_dorm():
  dorm = raw_input("Where will you be living? ")
  dorm = dorm.lower()
  a = ['mews','mews hall']
  b = ['townhouse','townhouse community']
  c = ['balch','balch Hall']
  d = ['clara dickson','clara dickson hall']
  e = ['bauer','court-kay-bauer','court kay bauer','court-kay-bauer hall','court kay bauer hall']
  f = ['high rise','high rise','high rise #5','high rise #5']
  g = ['jameson','jameson Hall']
  h = ['low rise','low rise','low-rise #6','low-rise #6','low rise #6','low rise #6','low-rise #6','low-rise #6']
  i = ['Low-rise #7','Low-Rise #7','low rise #7','low rise #7','low-rise #7','low-rise #7']
  j = ['mary Donlon','mary donlon hall','mary','mary hall','donlon','donolon hall']

  if dorm == a:
    return random()*1
  elif dorm == b:
    return random()*1
  elif dorm == c:
    return random()*1
  elif dorm == d:
    return random()*1
  elif dorm == e:
    return random()*1
  elif dorm == f:
    return random()*1
  elif dorm == g:
    return random()*1
  elif dorm == h:
    return random()*1
  elif dorm == i:
    return random()*1
  elif dorm == j:
    return random()*1
  else:
    print 'invalid response'