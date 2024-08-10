import requests

# URL of a free and SSL-verified text file
url = 'https://www.gutenberg.org/files/84/84-0.txt'

# Send a GET request to the URL
response = requests.get(url)

print(len(response.text))
print(response.raise_for_status)  # Resonse 200 means OK, while 404 is error
print(response.text[:550])
