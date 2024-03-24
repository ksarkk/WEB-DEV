def centered_average(nums):
  nums.sort()
  cnt = 0
  sum = 0
  for i in range(1, len(nums)-1):
    sum+=nums[i]
    cnt+=1
  return sum/cnt