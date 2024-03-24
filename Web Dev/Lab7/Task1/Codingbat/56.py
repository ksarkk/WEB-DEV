def make_chocolate(small, big, goal):
  if goal <= small: res = small
  
  elif big > 0:
    for i in range(big, 0, -1):
      if goal - (5*i) <= small and goal-(5*i) >=0:
        res = goal-(5*i)
        break
      else: res = -1
      
  else:res = -1
   
  return res
