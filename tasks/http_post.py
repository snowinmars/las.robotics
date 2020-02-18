import requests

uri = 'https://httpbin.org/post'

todo = {
    'id': 1,
    'title': 'custom title',
    'completed': True
}

response = requests.post(uri, data=todo)

print(response)
