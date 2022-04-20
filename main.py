from bs4 import BeautifulSoup
import requests

url = 'https://25livepub.collegenet.com/s.aspx?calendar=mc-all_advertised_events&widget=main&spudformat=xhr'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')


table = soup.find("table", class_="twSimpleTableTable") #GETS THE WHOLE TABLE


event_names = table.find_all('span', class_='twDescription')
for event_name in event_names:
    print(event_name.text) # gets all event names
    break

print('*' * 80)

all_start_times = table.find_all('span', class_='twStartTime')
for event in all_start_times:
    print(event.text) # gets all start times
    break

print('*' * 80)

all_locations = table.find_all('span', class_='twLocation')
for location in all_locations:
    print(location.text) # gets all locations
    break
    
print('*' * 80)

all_dates = table.find_all('div', class_='twSimpleTableGroupHead')
for date in all_dates:
    print(date.text) # gets all dates
    break
