def sum67(nums):
  cnt = 0
  ok = False
  for i in nums:
    if i == 6:
      ok = True
      continue
    if i == 7 and ok:
      ok = False
      continue
    if not ok:  
      cnt += i
  
  return cnt