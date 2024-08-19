import re
import random
import json
from bson import ObjectId
from faker import Faker

# Initialize Faker
faker = Faker()

def parse_kotlin_data_class(kotlin_class: str, num_of_records: int):
    # Remove single-line comments
    kotlin_class = re.sub(r'//.*', '', kotlin_class)
    
    # Remove block comments
    kotlin_class = re.sub(r'/\*.*?\*/', '', kotlin_class, flags=re.DOTALL)
    
    # Extract fields from the Kotlin data class
    fields = re.findall(r'val\s+(\w+):\s+([\w<>]+)', kotlin_class)
    
    records = []
    
    for _ in range(num_of_records):
        record = {}
        for field_name, field_type in fields:
            record[field_name] = generate_dummy_data(field_name, field_type)
        records.append(record)
    
    return records

def generate_dummy_data(field_name: str, field_type: str):
    # Handle specific types
    if 'Int' in field_type or 'Long' in field_type:
        return random.randint(1, 100)
    elif 'String' in field_type:
        return faker.word()
    elif 'List<String>' in field_type:
        return [faker.word() for _ in range(3)]
    elif 'Boolean' in field_type:
        return False
    elif 'BigDecimal' in field_type or 'Double' in field_type:
        return round(random.uniform(1.0, 100.0), 2)
    elif 'ObjectId' in field_type or 'id' in field_name or '_id' in field_name:
        return str(ObjectId())
    elif 'List' in field_type:
        return []
    else:
        return None  # Default for unknown types

def main():
    # Hardcoded Kotlin data class for testing
    kotlin_data_class = """
 data class Comments(
    val id: String,/*this is what will be used to odder the comments*/
    val name: String,
    val userId: String,
    val table: String,/*will decide which comment this is:for products,for services  etc*/
    val tableId: String,/*this is the id of the product/service/shop etc. in question*/
    val tableImage: String,/*this is the image of the object in question*/
    val comment: String,
    val time: String,/*format should be time/day(acronym)/date/month/year*/
    val likes: Long = 0,
    val replies: Long = 0
)

"""
    
    # User input for number of records
    num_of_records = int(input("Please enter the number of JSON records you want to generate:\n"))
    
    # Generate dummy data
    generated_data = parse_kotlin_data_class(kotlin_data_class, num_of_records)
    
    # Print the JSON data as a list
    print(json.dumps(generated_data, indent=4))

if __name__ == "__main__":
    main()
