def xyz_there(str):
  cnt1 = 0
  cnt2 = 0
  for i in range(len(str)-1):
    cnt1 += str[i:i+3] == 'xyz'
    cnt2 += str[i:i+4] == '.xyz'
    
  if cnt1>cnt2:
    return True
  else:
    return False