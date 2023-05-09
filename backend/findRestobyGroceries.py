import json
from urllib.request import urlopen
import geopy.distance



url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)
print(data)

coordinatesString=data["loc"]
tempUserLatitude=coordinatesString[0:7]
tempUserLongitude=coordinatesString[8:16]
print(tempUserLatitude)
print(tempUserLongitude)

    
    
# Define user's latitude and longitude
userLatitude = float(tempUserLongitude) #45.49311
userLongitude = float(tempUserLatitude)#-73.78726

dictionaryStore = {
    "Marche West Island": ["pineapple", "chicken", "apple"],
    "Jaffna Fruits": ["pineapple", "chicken", "apple"]
}

dictionaryAddressStore = [
    {
        "name": "Marche West Island",
        "latitude": 45.50417,
        "longitude": -73.77868
    },
    {
        "name": "Jaffna Fruits",
        "latitude": 45.50646,
        "longitude": -73.82878
    }
]

def globalFunction(grocery):

    def findRestobyGroceries(grocery):
        stores = []
        for resto in dictionaryStore:
            if grocery in dictionaryStore[resto]:
                for address in dictionaryAddressStore:
                    if address["name"] == resto:
                        stores.append({
                        "name": resto,
                        "latitude": address["latitude"],
                        "longitude": address["longitude"]
                    })
                    break
    
        return stores

    def calculateShortestDistance(matched_stores, user_latitude, user_longitude):
        closestStore = None
        closestDistance = float('inf')
        user_coordinates = (user_latitude, user_longitude)

        for store in matched_stores:
            store_latitude = store["latitude"]
            store_longitude = store["longitude"]
            store_coordinates = (store_latitude, store_longitude)

            distance = geopy.distance.distance(user_coordinates, store_coordinates).km
            if distance < closestDistance:
                closestDistance = distance
                closestStore = store

        return closestStore, closestDistance

    
    grocery = "pineapple"
    matched_stores = findRestobyGroceries(grocery)

    closest_store, distance = calculateShortestDistance(matched_stores, userLatitude, userLongitude)

    if closest_store is not None:
        print(f"The closest store is {closest_store['name']}")
        print(f"The distance is approximately {distance} kilometers")
    else:
        print("No stores found")

if __name__=="__main__":
    print(globalFunction("pineapple")) #itslikecallingtheAPI