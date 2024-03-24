def make_bricks(small, big, goal):
  if small<(goal%5) or (small+big*5)<goal: return False
  else: return True