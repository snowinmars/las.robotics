from _lib import User
import json

child = User("child", 13)
mother = User("mother", 31)

# lambda is required due to default serialization doesn't know how to serialize a custom class
data = json.dumps(mother, default=lambda x: x.__dict__)
filename = 'ser.output'

with open(filename, 'w') as file:
    file.write(data)

