import requests
from bs4 import BeautifulSoup


response = requests.get('https://askdjango.github.io/lv1/')

print(response)
print(response.text)
