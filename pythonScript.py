import math

# Earth's radius in km
EARTH_RADIUS_KM = 6371

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = EARTH_RADIUS_KM * c
    return distance

locations = [
    (-0.7899078000952, 36.85117627991967),
    (-0.7905850045974462, 36.85978314616029),
    (-0.7914122788132107, 36.86837688536974),
    (-0.7923893708365977, 36.87695488093333),
    (-0.7935159831420326, 36.885514521027304),
    (-0.7947917726748628, 36.89405319941362),
    (-0.7962163509558199, 36.90256831623308),
    (-0.7977892841993136, 36.911057278796406)
]

within_radius = True

for i in range(len(locations)):
    for j in range(i + 1, len(locations)):
        lat1, lon1 = locations[i]
        lat2, lon2 = locations[j]
        distance = haversine(lat1, lon1, lat2, lon2)
        if distance > 10:
            within_radius = False
            print(f"Location {locations[i]} and {locations[j]} are {distance:.2f} km apart, which is greater than 5 km.")
            break

if within_radius:
    print("All locations are within 5 km of each other.")
else:
    print("Not all locations are within 5 km of each other.")
