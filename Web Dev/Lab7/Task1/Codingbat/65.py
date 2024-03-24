def cat_dog(str):
  cnt1 = 0
  cnt2 = 0
  for i in range(len(str)-1):
    cnt1 += str[i:i+3] == 'cat'
    cnt2 += str[i:i+3] == 'dog'
  
  if cnt1==cnt2: return True
  return False
