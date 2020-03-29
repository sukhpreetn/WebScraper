import  pandas as pd
import requests
from bs4 import BeautifulSoup


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=36.37410569300005&lon=-119.27022999999997#.XoEYj5NKg_U')
soup = BeautifulSoup(page.content,'html.parser')
weekdata  = soup.find(id='seven-day-forecast-body')
#print(weekdata)
#print(weekdata.find_all('li'))
items = weekdata.find_all(class_='tombstone-container')
#print(items[0])

#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
#print(items[0].find(class_='temp').get_text())


period_names =  [item.find(class_='period-name').get_text() for item in items]
short_description =  [item.find(class_='short-desc').get_text() for item in items]
temperatures =  [item.find(class_='temp').get_text() for item in items]
#print(period_names)
#print(short_description)
#print(temperatures)

weather_data = pd.DataFrame(
    {
        'period'                : period_names,
        'short_descriptions'    : short_description,
        'temperatues'           : temperatures,
    }
)

print(weather_data)

weather_data.to_csv('weather.csv')
