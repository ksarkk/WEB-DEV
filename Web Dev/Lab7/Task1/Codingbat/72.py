def has22(nums):
  found = False
  for i in range(0, len(nums)-1):
    if i>0 and nums[i]==2 and nums[i-1]==2:
      found = True
    if nums[i]==2 and nums[i+1]==2 and i<len(nums)-1:
      found = True
    else: found = False
  return found