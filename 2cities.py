import geopy
from geopy.distance import geodesic

mumbai = (19.0760, 72.8777)
raipur = (21.2514, 81.6296)

print("distance b/w mumbai & raipur: ",geodesic(mumbai, raipur).km)