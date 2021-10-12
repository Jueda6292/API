import geocoder
import requests

API_KEY = 'XXXXXXXXXXXXXXXXXXXX'

API_BASE_URL = f'httpsapi.openweathermap.orgdata2.5weatherunits=imperial&appid={API_KEY}'

def main()
  destinations = ['Space Needle', 
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada',
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'ellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge',
  ]

  for destination in destinations
    g = geocoder.arcgis(destination)
    print (f'The {destination} is located at ({g.latlng[0].2f}, {g.latlng[1].2f})')

    lat = f'{g.latlng[0].2f}'
    lng = f'{g.latlng[1].2f}'

    full_api_url = API_BASE_URL + '&lat=' + lat + '&lon=' + lng
    
    
    result = requests.get(full_api_url).json()

    print(fAt the {destination} right now, it's {result['weather'][0]['description']} with a temperature of {result['main']['temp'].1f}u00B0Fn)


main()
