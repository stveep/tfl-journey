import requests 
import urlparse

start_points = ["SW1A1AA", "E202ST", "51.505896,-0.166802", "W1A1AA"]
end_point = "SW36JB"
date = "20170904"
time = "0800"

def plan_journey(start_point, end_point, date, time):
  url = "https://api.tfl.gov.uk/Journey/JourneyResults/" + start_point + "/to/" + end_point
  payload = {'date': date, 'time': time}
  return requests.get(url, payload).json()

# Response structure:
# {"journeys": [
#   {"duration" ... "legs": [
#                              { "duration" ... "mode": { "name" ... } }
def durations(response):
  return map(lambda x: x['duration'], response['journeys'])

for i in start_points:
  r = plan_journey(i, end_point, date, time)
  print i + "\t" + str(min(durations(r)))

