import requests

def main():
	uri = 'https://jsonplaceholder.typicode.com/posts/1'

	data = requests.get(uri).json()

	print(data)
	print(data['userId'])

main()