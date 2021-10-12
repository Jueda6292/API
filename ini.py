import geocoder

def main():
  # Declare destinations list here
  destinations = ['Space Needle', 
    'Crater Lake',
    'Golden Gate Bridge',
    'Yosemite National Park',
    'Las Vegas, Nevada'
    'Grand Canyon National Park',
    'Aspen, Colorado',
    'Mount Rushmore',
    'ellowstone National Park',
    'Sandpoint, Idaho',
    'Banff National Park',
    'Capilano Suspension Bridge',
  ]

  # Loop through each destination
  for destination in destinations:
      g=geocoder.arcgis(destination)
      print (f'{destination} is located at ({g.latlng[0]:.2f}, {g.latlng[1]:.2f})')
    #   Get the lat-long coordinates from `geocoder.arcgis`
    #   Print out the place name and the coordinates

main()
