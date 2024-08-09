import json
import random
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

def generate_locations(reference_location, num_locations, radius):
    locations = []
    ref_lat, ref_lon = reference_location
    
    while len(locations) < num_locations:
        # Randomly generate a location within the radius
        distance = random.uniform(0, radius)
        angle = random.uniform(0, 2 * math.pi)
        
        # Calculate new location
        dlat = distance / EARTH_RADIUS_KM
        dlon = distance / (EARTH_RADIUS_KM * math.cos(math.radians(ref_lat)))
        
        new_lat = ref_lat + math.degrees(dlat)
        new_lon = ref_lon + math.degrees(dlon) * math.cos(angle)
        
        if haversine(ref_lat, ref_lon, new_lat, new_lon) <= radius:
            locations.append((new_lat, new_lon))
    
    return locations

def main():
    reference_location = (34.8244991, -0.8237814)  # Reference location
    num_locations = 7
    max_radius = 5  # Maximum radius in km
    
    locations = generate_locations(reference_location, num_locations, max_radius)
    
    # Ensure at least 2 locations are within 3 km of the reference location
    within_3km = [loc for loc in locations if haversine(reference_location[0], reference_location[1], loc[0], loc[1]) <= 3]
    
    while len(within_3km) < 2:
        new_location = generate_locations(reference_location, 2 - len(within_3km), 3)
        within_3km.extend(new_location)
    
    locations = within_3km[:2] + locations[:5]  # Ensure we have at least 7 locations
    
    # Create JSON data
    json_data = {
        "locations": [
            {"longitude": lon, "latitude": lat} for lat, lon in locations
        ]
    }
    
    # Print JSON output
    print(json.dumps(json_data, indent=2))

if __name__ == "__main__":
    main()
