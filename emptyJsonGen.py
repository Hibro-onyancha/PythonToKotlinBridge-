import re
import json

def kotlin_data_class_to_json(kotlin_class: str) -> str:
    # Remove single-line comments
    kotlin_class = re.sub(r'//.*', '', kotlin_class)

    # Remove multi-line comments
    kotlin_class = re.sub(r'/\*.*?\*/', '', kotlin_class, flags=re.DOTALL)

    # Regex to match property definitions in Kotlin data class
    pattern = r'val\s+(\w+):\s+([\w\?\<\>]+)(\s*=\s*[^,]*)?'
    matches = re.findall(pattern, kotlin_class)

    json_dict = {}
    
    for match in matches:
        prop_name, prop_type, default_value = match

        # Determine the JSON equivalent value based on Kotlin type
        if prop_type.endswith("?"):
            json_dict[prop_name] = None
        elif prop_type.startswith("String"):
            json_dict[prop_name] = ""
        elif prop_type.startswith("Int") or prop_type.startswith("Long"):
            json_dict[prop_name] = 0
        elif prop_type.startswith("Double") or prop_type.startswith("Float"):
            json_dict[prop_name] = 0.0
        elif prop_type.startswith("Boolean"):
            json_dict[prop_name] = False
        elif prop_type.startswith("List<") and prop_type.endswith(">"):
            inner_type = prop_type[5:-1]  # Extract inner type from List<>
            if "listOf" in default_value:
                json_dict[prop_name] = []
            elif inner_type not in ["String", "Int", "Long", "Double", "Float", "Boolean"]:
                json_dict[prop_name] = []
            else:
                json_dict[prop_name] = []
        elif prop_type.startswith("List"):
            json_dict[prop_name] = []
        elif prop_type not in ["String", "Int", "Long", "Double", "Float", "Boolean"]:
            json_dict[prop_name] = None
        else:
            json_dict[prop_name] = {}

    # Convert dictionary to JSON string
    return json.dumps(json_dict, indent=4)

# Ask the user to input the Kotlin data class
print("Please enter your Kotlin data class (end input with an empty line):")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
kotlin_class = "\n".join(lines)

# Convert Kotlin data class to JSON
json_output = kotlin_data_class_to_json(kotlin_class)
print("\nGenerated JSON:")
print(json_output)
