def alarm_clock(day, vacation):
  if not vacation: week_preset = "7:00"
  else:  week_preset = "10:00"
  if not vacation:  weekend_preset = "10:00"
  else:  weekend_preset =  "off"
  
  if day not in [6,0]:return week_preset
  else: return weekend_preset
  