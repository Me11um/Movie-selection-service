from bs4 import BeautifulSoup
import requests
import random

def getmoviesname(genre):
    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'
          }

    url = 'https://www.kinoafisha.info/rating/movies/' + genre + '/'
    if genre == 'default':
        url = 'https://www.kinoafisha.info/rating/movies/'
    page = requests.get(url, headers = headers)

    movies = []

    filteredmovies = []
    filteredimages = []
    filteredgenre = []
    filteredyear = []
    filteredrating = []
    filteredhref = []

    soup = BeautifulSoup(page.text, "html.parser")
    movies = soup.findAll('a' , class_='movieItem_title')
    images = soup.findAll('img' , class_='picture_image')
    moviesgenre = soup.findAll('span', class_='movieItem_genres')
    moviesyear = soup.findAll('span', class_='movieItem_year')
    moviesrating = soup.findAll('span', class_='miniRating')

    nums = []

    for i in range(3):
        if i == 0:
            nums.append(random.randint(0, len(movies) - 1))
        else:
            nums.append(random.randint(0, len(movies) - 1))
            while nums[i] == nums[i - 1]:
                nums[i] = random.randint(0, len(movies) - 1)

    for i in nums:
        filteredmovies.append(movies[i].text)
        filteredimages.append(images[i]['data-picture'])
        filteredgenre.append(moviesgenre[i].text)
        filteredyear.append(moviesyear[i].text)
        filteredrating.append("рейтинг: " + moviesrating[i].text)
        filteredhref.append(movies[i]['href'])


    rdata = {
        'movies': filteredmovies,
        'images': filteredimages,
        'genre': filteredgenre,
        'year': filteredyear,
        'rating': filteredrating,
        'hrefs': filteredhref
    }

    return rdata
    #print(filteredimages)