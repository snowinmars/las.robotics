from _lib import User
import json

# lambda is required due to default serialization doesn't know how to serialize a custom class
# data = json.dumps(mother, default=lambda x: x.__dict__)

with open('ser.output', 'r') as file:
    data = json.load(file)
    mother = User(data['name'], data['age'])


mother.print()
