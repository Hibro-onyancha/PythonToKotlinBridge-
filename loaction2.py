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

def locations_within_radius(locations, radius):
    within_radius_locations = []
    
    for i in range(len(locations)):
        lat1, lon1 = locations[i]
        for j in range(i + 1, len(locations)):
            lat2, lon2 = locations[j]
            distance = haversine(lat1, lon1, lat2, lon2)
            if distance <= radius:
                if (lat1, lon1) not in within_radius_locations:
                    within_radius_locations.append((lat1, lon1))
                if (lat2, lon2) not in within_radius_locations:
                    within_radius_locations.append((lat2, lon2))
    
    return within_radius_locations

# Example locations
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

# Input radius
radius = float(input("Enter the radius (in km): "))

# Get locations within the specified radius
result = locations_within_radius(locations, radius)

# Output the result
if result:
    print(f"Locations within {radius} km radius:")
    for loc in result:
        print(f"Latitude: {loc[0]}, Longitude: {loc[1]}")
else:
    print(f"No locations are within {radius} km radius.")
