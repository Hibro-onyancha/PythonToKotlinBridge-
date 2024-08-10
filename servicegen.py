import json
import random
from bson import ObjectId

def generate_random_location(center_location, radius_km):
    radius_deg = radius_km / 110.574
    delta_lat = random.uniform(-radius_deg, radius_deg)
    delta_lon = random.uniform(-radius_deg, radius_deg)
    return {
        "longitude": center_location["longitude"] + delta_lon,
        "latitude": center_location["latitude"] + delta_lat
    }

def generate_service_data(num_services, center_location, radius_km):
    services = []
    for _ in range(num_services):
        service = {
            "id": str(ObjectId()),
            "name": f"Service {_ + 1}",
            "owner": f"Owner {_ + 1}",
            "standardPrice": random.randint(100, 10000),
            "image": f"https://example.com/image{_ + 1}.jpg",
            "location": generate_random_location(center_location, radius_km),
            "pricing": [],
            "posts": random.randint(0, 100),
            "likes": random.randint(0, 1000),
            "dislikes": random.randint(0, 100),
            "comments": random.randint(0, 1000),
            "followers": random.randint(0, 1000),
            "flags": random.randint(0, 100),
            "about": f"This is a description of Service {_ + 1}"
        }
        services.append(service)
    return services

center_location = {
    "longitude": 34.8244991,
    "latitude": -0.8237814
}

services = generate_service_data(5, center_location, 5)

# Convert to JSON
services_json = json.dumps(services, indent=2)
print(services_json)