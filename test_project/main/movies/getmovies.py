from bs4 import BeautifulSoup
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'
      }

url = 'https://www.kinoafisha.info/rating/movies/'
page = requests.get(url, headers = headers)
print(page.status_code)

movies = []
filteredmovies = []
filteredimages = []

soup = BeautifulSoup(page.text, "html.parser")
movies = soup.findAll('a' , class_='movieItem_title')
images = soup.findAll('img' , class_='picture_image')

for data in movies:
    filteredmovies.append(data.text)

for data in images:
    filteredimages.append(data['data-picture'])

#print(filteredimages)