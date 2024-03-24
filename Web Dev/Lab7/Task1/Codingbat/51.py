def squirrel_play(temp, is_summer):
  if is_summer == True and temp in range(60,101): return True
  elif is_summer == False and temp in range(60, 91): return True
  else: return False