from random import randint
def intended_dorm():
  dorm = raw_input("What is the name of your dorm for the academic school-year in Cornell")
  a = 'Mews' or 'Mews Hall'
  b = 'Townhouse' or 'Townhouse Community'
  c = 'Balch' or 'Balch Hall'
  d = 'Clara Dickson' or 'Clara Dickson Hall'
  e = 'Bauer' or 'Court-Kay-Bauer' or 'Court Kay Bauer' or 'Court-Kay-Bauer Hall' or 'Court Kay Bauer Hall'
  f = 'High Rise' or 'High rise' or 'High Rise #5' or 'High rise #5'
  g = 'Jameson' or 'Jameson Hall'
  h = 'low rise' or 'Low Rise' or 'Low-rise #6'  or 'Low-Rise #6' or 'low rise #6' or 'Low Rise #6' or 'Low-rise #6' or 'Low-Rise #6' 
  i = 'Low-rise #7'  or 'Low-Rise #7' or 'low rise #7' or 'Low Rise #7' or 'Low-rise #7' or 'Low-Rise #7'
  j = 'Mary Donlon' or 'Mary Donlon Hall' or 'Mary' or 'Mary Hall' or 'Donlon' or 'Donolon Hall'
  if dorm == a or a.lower() or a.upper():
    return randint(1,10) 
  elif dorm == b or b.lower() or b.upper():
    return randint(21,30)
  elif dorm == c or c.lower() or b.upper():
    return randint(31,40)
  elif dorm == d or d.lower() or b.upper():
    return randint(41,50)
  elif dorm == e or e.lower() or b.upper():
    return randint(51,60)
  elif dorm == f or f.lower() or b.upper():
    return randint(61,70)
  elif dorm == g or g.lower() or b.upper():
    return randint(71,80)
  elif dorm == h or h.lower() or b.upper():
    return randint(81,90)
  elif dorm == i or i.lower() or b.upper():
    return randint(91,110)
  elif dorm == j or j.lower() or b.upper():
    return randint(111,120)
  else:
    print 'invalid response'
    
    