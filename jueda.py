import geocoder
import requests

# Replace XXXXXXXXXXXX with your actual key, which
# will look like a bunch of letters and numbers!
API_KEY = 'd3e16c7696a98c3c5da244d73bcb0a0d'
# When you are done with the homework, remove your actual key
# and replace it back with XXXXXXXXXXXXXXXXXX before you commit
# and push to Github.

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

  # Loop through each destination
  for destination in destinations
    g = geocoder.arcgis(destination)
    print (f'The {destination} is located at ({g.latlng[0].2f}, {g.latlng[1].2f})')
    ###########
    # COPY & PASTE RELEVANT CODE FROM PART 1 HERE
    ###########

    # You'll need to construct the full API url with the latitude and longitude,
    # with something like this
    # full_api_url = API_BASE_URL + '&lat=' + latitude + '&lon=' + longitude

    lat = f'{g.latlng[0].2f}'
    lng = f'{g.latlng[1].2f}'

    full_api_url = API_BASE_URL + '&lat=' + lat + '&lon=' + lng
    
    
    result = requests.get(full_api_url).json()

    print(fAt the {destination} right now, it's {result['weather'][0]['description']} with a temperature of {result['main']['temp'].1f}u00B0Fn)
    # result = requests.get(full_api_url).json()


    # From the result, print ousummaryt the  and current temperature


main()
