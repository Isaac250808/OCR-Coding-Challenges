def mphAverage(time1, time2, distance):
  hh1 = int(time1[0]+time1[1])
  mm1 = int(time1[3]+time1[4])
  ss1 = int(time1[6]+time1[7])
  hh2 = int(time2[0]+time2[1])
  mm2 = int(time2[3]+time2[4])
  ss2 = int(time2[6]+time2[7])
  total1 = hh1*3600+mm1*60+ss1
  total2 = hh2*3600+mm2*60+ss2
  hour1 = total1/3600
  hour2 = total2/3600
  hour = hour2-hour1
  if hour < 0:
    hour = hour + 24
  mph = distance/hour
  return mph


def checkFormat(plate):
  flag = True
  if len(plate) != 8:
    flag = False
  else:
    if plate[0].isalpha() != True or plate[1].isalpha() != True or plate[2].isdigit() != True or plate[3].isdigit() != True or plate[5].isalpha() != True or plate[6].isalpha() != True or plate[7].isalpha() != True or not(plate[4].isdigit() == False and plate[4].isalpha() == False):
      flag = False
  return flag

# Time in the format of hh:mm:ss
print(mphAverage("08:56:37","08:58:42",1))

# Numberplate in the format of XXXX XXX (WITH SPACE IN, if a space)
print("The number plate is in the correct format:", checkFormat("EN54 UYA"))
