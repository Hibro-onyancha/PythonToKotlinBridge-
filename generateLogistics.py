import json
import random
import math
from faker import Faker

fake = Faker()

# Helper function to generate random locations within a given radius
def generate_random_location(center_lat, center_lon, radius_km):
    radius_m = radius_km * 1000
    angle = random.uniform(0, 2 * math.pi)
    distance = random.uniform(0, radius_m)
    lat_offset = distance * math.cos(angle) / 111320  # 1 degree latitude ~ 111.32 km
    lon_offset = distance * math.sin(angle) / (111320 * math.cos(center_lat * math.pi / 180))  # Adjust for longitude
    
    return {
        "latitude": center_lat + lat_offset,
        "longitude": center_lon + lon_offset
    }

# Function to generate random LogisticTime objects
def generate_logistic_time():
    return {
        "maxTime": fake.time(pattern="%H:%M:%S"),
        "minTime": fake.time(pattern="%H:%M:%S"),
        "days": random.sample(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], 3)
    }

# Function to generate Logistics objects
def generate_logistics(num_logistics, center_lat, center_lon, radius_km):
    logistics_list = []
    
    for _ in range(num_logistics):
        logistics = {
            "id": "ObjectId(\"" + fake.uuid4() + "\")",
            "name": fake.company(),
            "owner": fake.name(),
            "location": generate_random_location(center_lat, center_lon, radius_km),
            "areas": [generate_random_location(center_lat, center_lon, radius_km) for _ in range(random.randint(1, 3))],
            "maxLoad": random.randint(1000, 10000),
            "minLoad": random.randint(100, 1000),
            "vehicleType": fake.word(),
            "likes": random.randint(0, 1000),
            "dislikes": random.randint(0, 1000),
            "comments": random.randint(0, 1000),
            "followers": random.randint(0, 1000),
            "flags": random.randint(0, 1000),
            "about": fake.text(max_nb_chars=100),
            "workingTime": [generate_logistic_time() for _ in range(random.randint(1, 3))],
            "synonyms": [fake.word() for _ in range(random.randint(1, 5))]
        }
        logistics_list.append(logistics)
    
    return logistics_list

# Main function to handle user input and generate JSON
def main():
    center_location = {
        "longitude": 34.8244991,
        "latitude": -0.8237814
    }
    radius_km = 3
    num_logistics = int(input("Enter the number of Logistics to generate: "))
    
    logistics_list = generate_logistics(num_logistics, center_location["latitude"], center_location["longitude"], radius_km)
    
    # Convert to JSON
    json_output = json.dumps(logistics_list, indent=4)
    print("\nGenerated JSON:")
    print(json_output)

if __name__ == "__main__":
    main()
