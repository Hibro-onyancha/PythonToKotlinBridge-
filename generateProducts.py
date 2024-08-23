import json
import random
import math
from bson import ObjectId

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

def generate_location(reference_location, radius):
    ref_lat, ref_lon = reference_location
    
    # Randomly generate a location within the radius
    distance = random.uniform(0, radius)
    angle = random.uniform(0, 2 * math.pi)
    
    # Calculate new location
    dlat = distance / EARTH_RADIUS_KM
    dlon = distance / (EARTH_RADIUS_KM * math.cos(math.radians(ref_lat)))
    
    new_lat = ref_lat + math.degrees(dlat)
    new_lon = ref_lon + math.degrees(dlon) * math.cos(angle)
    
    return (new_lat, new_lon)

def generate_product_data(num_products, radius, reference_location):
    products = []
    
    for _ in range(num_products):
        location = generate_location(reference_location, radius)
        product = {
            "id": str(ObjectId()),
            "shopId": "245",
            "dateUpdated": "2024-08-08T00:00:00Z",
            "name": f"Product_{_+1}",
            "category":"pasta",
            "price": random.randint(100, 1000),
            "soldItems": random.randint(0, 100),
            "remainingItems": random.randint(0, 100),
            "totalPriceSold": random.randint(1000, 10000),
            "location": {
                "longitude": location[1],
                "latitude": location[0]
            },
            "productDesc": f"Description for product {_+1}",
            "images": [str(ObjectId()) for _ in range(random.randint(1, 3))],
            "userAddId": str(ObjectId()),
            "maxBargainValue": random.randint(0, 100),
            "minBargainValue": random.randint(0, 50),
            "discountState": random.randint(0, 2),
            "showDiscountAsMainPrice": random.choice([True, False]),
            "shouldShowRemainingItems": random.choice([True, False]),
            "currentPrice": random.randint(50, 500),
            "startingProducts": random.randint(0, 100),
            "isPinned": random.choice([True, False]),
            "synonyms": [f"Synonym_{_+1}"],
            "allSoldProducts": random.randint(0, 100),
            "isPrivate": random.choice([True, False]),
            "priceSuffix": "USD",
            "likes": random.randint(0, 100),
            "diLikes": random.randint(0, 100),
            "comments": random.randint(0, 50),
            "flags": random.randint(0, 50),
            "cartAdds": random.randint(0, 50)
        }
        products.append(product)
    
    return products

def main():
    reference_location = (34.8244991, -0.8237814)  # Reference location
    num_products = 5
    radius = float(input("Enter the radius in km: "))
    
    products = generate_product_data(num_products, radius, reference_location)
    
    # Create JSON data
    json_data = {
        "products": products
    }
    
    # Print JSON output
    print(json.dumps(json_data, indent=2))

if __name__ == "__main__":
    main()
