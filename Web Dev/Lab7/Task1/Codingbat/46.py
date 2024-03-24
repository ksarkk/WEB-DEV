def caught_speeding(speed, is_birthday):
  spd = 0
  if is_birthday: spd = 65
  else: spd = 60
  ans = speed - spd
  if ans > 20: return 2
  elif ans > 0: return 1
  else:return 0
