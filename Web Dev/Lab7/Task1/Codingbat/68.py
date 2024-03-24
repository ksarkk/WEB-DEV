def sum13(nums):
  sum = 0
  for i in range(0, len(nums)):
    if nums[i]!=13: 
      sum+=nums[i]
      if i>0 and nums[i-1] == 13: sum-=nums[i]
  return sum