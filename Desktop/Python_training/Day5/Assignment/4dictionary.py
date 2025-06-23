# Original dictionary
original_dict = {
    'name': 'Raj',
    'age': 25,
    'gender': 'male',
    'city': 'Trihy',
    'country': 'India'
}

# Keys you want to extract
keys_to_extract = ['name', 'city']

try:
# Create new dictionary
    new_dict = {key: original_dict[key] for key in keys_to_extract}

except KeyError as e:
    print(f'Key not found {e}')
    new_dict = {}

print("Extracted Dictionary:", new_dict)
