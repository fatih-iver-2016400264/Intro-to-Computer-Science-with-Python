from geopy.distance import vincenty
import random
import time

temperature = 18.9
coordinates = (36.549362, 31.996994)

while True:
    print("Log: %s" % time.ctime(), end = '')
    print(" Elapsed Time 5 seconds")
    
    deltaX = random.uniform(-0.0001, 0.0001)
    deltaY = random.uniform(-0.0001, 0.0001)
    deltaTemp = random.uniform(-0.4, 0.4)
    
    newCoordinates = (coordinates[0] + deltaX, coordinates[1] + deltaY)
    
    print("Distance:" + str(vincenty(newCoordinates, coordinates).meters) + " meters")
    
    coordinates = newCoordinates  
    temperature += deltaTemp
    
    print("Temperature: " + str(temperature))
    print("Coordinates:" + str(coordinates))
    print()
   
    time.sleep(5)