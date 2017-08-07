import requests 
from numpy import arange
import csv

end_point = "SW36JB"
date = "20170904"
time = "0800"

def plan_journey(start_point, end_point, date, time):
  url = "https://api.tfl.gov.uk/Journey/JourneyResults/" + start_point + "/to/" + end_point
  payload = {'date': date, 'time': time}
  r = requests.get(url, payload)
  if r.status_code == requests.codes.ok:
    return r.json()
  else:
    return False # Fails silently if the request fails

# Response structure:
# {"journeys": [
#   {"duration" ... "legs": [
#                              { "duration" ... "mode": { "name" ... } }
def durations(response):
  return map(lambda x: x['duration'], response['journeys'])


locations = []
header = True
with open('stations.csv', 'rb') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader: 
    if header:
      header = False
      next
    # Filter by Zone:
    elif row[5] in ['1','2','3']:
      locations.append([row[0],row[6]])

for point in locations:
  r = plan_journey(point[1], end_point, date, time)
  if r:
    print point[0] + "\t" + str(min(durations(r)))

