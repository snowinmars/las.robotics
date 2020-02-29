from _lib import User
import json

def main():
    filename = 'ser.output'
    
    with open(filename, 'r') as file:
        data = json.load(file)
        mother = User(data['name'], data['age'])

    mother.print()

main()