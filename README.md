# API

* Use modules and packages
* Use data from APIs
* Read documentation for modules and APIs

## Deliverables

1. Write your code and solve the problems. Remember to **save** frequently

1. Run the program from the command line to check your work.

1. Keep making changes to your code and run it again until you get the expected output. Repeat as needed!

---
# Question 1
Cody and his friends Heather and Matt are going on a road trip across the Western United States and Canada. They want to visit several landmarks, national parks, and big cities.

Here's their agenda:

```
Space Needle
Crater Lake
Golden Gate Bridge
Yosemite National Park
Las Vegas, Nevada
Grand Canyon National Park
Aspen, Colorado
Mount Rushmore
Yellowstone National Park
Sandpoint, Idaho
Banff National Park
Capilano Suspension Bridge
```

Put these destinations into a list of strings called `destinations`.

Then, import the [geocoder](https://geocoder.readthedocs.io/providers/ArcGIS.html#geocoding) module, and use it to translate each of the landmarks into latitude-longitude coordinates. (This is an example of using an API through a **wrapper**.)

Now, loop through the list of locations, and print each location's latitude and longitude.

We will be using `arcgis` service to translate the places to coordinates. The `geocoder` module is a **wrapper** that wraps the `arcgis` service (among others) so you don't have to do it manually via HTTP requests.

Visit the [docs](https://geocoder.readthedocs.io) for more sample code.

## Expected Output

```
Space Needle is located at (47.6205, -122.3493)
Crater Lake is located at (42.8684, -122.1685)
Golden Gate Bridge is located at (37.8199, -122.4783)
Yosemite National Park is located at (37.8651, -119.5383)
Las Vegas, Nevada is located at (36.1699, -115.1398)
Grand Canyon National Park is located at (36.1070, -112.1130)
Aspen, Colorado is located at (39.1911, -106.8175)
Mount Rushmore is located at (43.8791, -103.4591)
Yellowstone National Park is located at (44.4280, -110.5885)
Sandpoint, Idaho is located at (48.2766, -116.5535)
Banff National Park is located at (51.4968, -115.9281)
Capilano Suspension Bridge is located at (49.3429, -123.1149)
```

---

# Ouestion 2

Cody is satisfied by geolocating his landmarks, but Heather wants to take it one step further and get the current weather at each location.

Help Heather with some code that calls an API to get current weather based on latitude-longitude coordinates. Use the [Open Weather Map API](https://home.openweathermap.org/users/sign_up) for this.

**Note:** You will need to register for an account to get an API key, but it is free to use (up to 60 calls per minute).

```
The Space Needle is located at (47.6205, -122.3492)
At The Space Needle right now, it's broken clouds with a temperature of 72.75
Crater Lake is located at (42.9116, -122.1483)
At Crater Lake right now, it's clear sky with a temperature of 69.37
The Golden Gate Bridge is located at (37.8191, -122.4785)
At The Golden Gate Bridge right now, it's clear sky with a temperature of 68.47
Yosemite National Park is located at (37.7490, -119.5885)
At Yosemite National Park right now, it's clear sky with a temperature of 85.66
Las Vegas, Nevada is located at (36.1719, -115.1400)
At Las Vegas, Nevada right now, it's clear sky with a temperature of 101.08
Grand Canyon National Park is located at (36.0573, -112.1096)
At Grand Canyon National Park right now, it's clear sky with a temperature of 86
Aspen, Colorado is located at (39.1900, -106.8182)
At Aspen, Colorado right now, it's clear sky with a temperature of 84.96
Mount Rushmore is located at (43.8803, -103.4588)
At Mount Rushmore right now, it's clear sky with a temperature of 77.04
Yellowstone National Park is located at (44.9775, -110.6983)
At Yellowstone National Park right now, it's clear sky with a temperature of 77.63
Sandpoint, Idaho is located at (48.2730, -116.5478)
At Sandpoint, Idaho right now, it's clear sky with a temperature of 78.28
Banff National Park is located at (51.1780, -115.5703)
At Banff National Park right now, it's broken clouds with a temperature of 75
Capilano Suspension Bridge is located at (49.3430, -123.1139)
At Capilano Suspension Bridge right now, it's scattered clouds with a temperature of 74.8
```

## Remove Your Key!

When you are done with Exercise 2, **remove your key from your source code file** before committing and pushing your code to Github!

---

# Question 3

Matt likes Heather's idea of getting the weather for each location they plan on visiting, but he thinks the data is unreadable.

Modify your code to:

1. Display a newline after each location (`\n`)
1. Display only one decimal place on the temperature (think about string formatting)
1. Display an F (for Fahrenheit)
1. Display a unicode degree (&deg;) character

### Expected Output

```
The Space Needle is located at (47.6205, -122.3492)
At The Space Needle right now, it's broken clouds with a temperature of 72.8°F

Crater Lake is located at (42.9116, -122.1483)
At Crater Lake right now, it's clear sky with a temperature of 69.4°F

The Golden Gate Bridge is located at (37.8191, -122.4785)
At The Golden Gate Bridge right now, it's clear sky with a temperature of 68.4°F

Yosemite National Park is located at (37.7490, -119.5885)
At Yosemite National Park right now, it's clear sky with a temperature of 85.7°F

Las Vegas, Nevada is located at (36.1719, -115.1400)
At Las Vegas, Nevada right now, it's clear sky with a temperature of 100.9°F

Grand Canyon National Park is located at (36.0573, -112.1096)
At Grand Canyon National Park right now, it's clear sky with a temperature of 86.0°F

Aspen, Colorado is located at (39.1900, -106.8182)
At Aspen, Colorado right now, it's clear sky with a temperature of 85.0°F

Mount Rushmore is located at (43.8803, -103.4588)
At Mount Rushmore right now, it's clear sky with a temperature of 77.0°F

Yellowstone National Park is located at (44.9775, -110.6983)
At Yellowstone National Park right now, it's clear sky with a temperature of 77.6°F

Sandpoint, Idaho is located at (48.2730, -116.5478)
At Sandpoint, Idaho right now, it's clear sky with a temperature of 78.3°F

Banff National Park is located at (51.1780, -115.5703)
At Banff National Park right now, it's broken clouds with a temperature of 75.0°F

Capilano Suspension Bridge is located at (49.3430, -123.1139)
At Capilano Suspension Bridge right now, it's scattered clouds with a temperature of 74.8°F
```

---

# Done and Done!

Too bad we don't have time for an actual road trip...

![](https://media.giphy.com/media/PqwqtOLfG19Ti/giphy.gif)
