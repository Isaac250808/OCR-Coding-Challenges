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

def breakSpeed(speed, limit):
    if speed > limit:
        return "is"
    else:
        return "is not"


def checkFormat(plate):
  flag = True
  if len(plate) != 8:
    flag = False
  else:
    if plate[0].isalpha() != True or plate[1].isalpha() != True or plate[2].isdigit() != True or plate[3].isdigit() != True or plate[5].isalpha() != True or plate[6].isalpha() != True or plate[7].isalpha() != True or not(plate[4].isdigit() == False and plate[4].isalpha() == False):
      flag = False
  if flag:
    return "is standard"
  else:
    return "is not standard"

# Time in the format of hh:mm:ss
print(mphAverage("08:56:37","08:58:42",1))

# Numberplate in the format of XXXX XXX (WITH SPACE IN, if a space)
en54 = "EN54 UYA"
print("The number plate", en54+"'s format", checkFormat(en54))

speedLimit = 70

f = open("plates.txt","r")
plates = f.readlines()
f.close()
for i in range(len(plates)):
    plates[i] = plates[i][0:-1].split(";")
#print(plates)
for i in plates:
    print()
    speedTemp = mphAverage(i[1],i[2],1)
    print("The car,",i[0],breakSpeed(speedTemp,speedLimit),"breaking the speed limit ("+str(mphAverage(i[1],i[2],1))[0:4]+"mph in a",str(speedLimit)+")")
    print("The number plate",i[0]+"'s format",checkFormat(i[0]))

