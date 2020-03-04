import requests
from bs4 import BeautifulSoup
import time
import json
import pandas as pd
from pandas.io.json import json_normalize

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:73.0) Gecko/20100101 Firefox/73.0'
}


def get_tmdb_ids(list_url):
    df_json = pd.read_json(list_url)
    df_norm = json_normalize(df_json['results'])
    resultant = pd.concat([df_json, df_norm], axis=1).drop('results', axis=1)

    return (list(resultant['id']))


def get_imdb_ID(tmdb_id):
    movie_url = 'https://api.themoviedb.org/3/movie/' + str(tmdb_id) +'?api_key=d34a7ae8e00fac4590a4aee2a6e5d4a5&language=en-US'
    print('Scraping: ' + movie_url)
    movie_resp = requests.get(movie_url, headers=headers)
    movie_json = movie_resp.json()
    imdb_id = movie_json['imdb_id']

    if imdb_id == None:
        imdb_id = 0
        print('No IMDb ID detected.')

    return imdb_id


def get_movie_details(tmdb_id):
    production_companies = []
    genres = []
    url = 'https://api.themoviedb.org/3/movie/' + str(tmdb_id) +'?api_key=d34a7ae8e00fac4590a4aee2a6e5d4a5&language=en-US'
    movie_resp = requests.get(url, headers=headers)
    movie_json = movie_resp.json()
    for p in movie_json['production_companies']:
        production_companies.append(p['name'])
    for z in movie_json['genres']:
        genres.append(z['name'])

    return movie_json['title'], movie_json['release_date'], movie_json['runtime'], movie_json['budget'], movie_json['original_language'], production_companies, genres


def get_box_office(imdb_id):
    if imdb_id == 0:
        print('get_box_office() cancelled')
        return 0

    url = 'https://www.boxofficemojo.com/title/' + imdb_id
    print('Getting box office information on: ' + url)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    money = soup.findAll('span', {'class': 'a-size-medium a-text-bold'})

    box_office = []

    x = 0
    while x < 3:
        box_office.append(money[x].get_text().strip())
        x += 1

    return box_office

def get_imdb_info(imdb_id):
    if imdb_id == 0:
        print('get_imdb_info() cancelled')
        return 0

    url = 'https://www.imdb.com/title/' + imdb_id
    print('Getting IMDb information on: ' + url)
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')

    time.sleep(1)
    imdb_info = []

    meta_score = soup.find('div', {'class': ['metacriticScore score_favorable titleReviewBarSubItem', 'metacriticScore score_mixed titleReviewBarSubItem', 'metacriticScore score_unfavorable titleReviewBarSubItem']})
    if meta_score == None:
        imdb_info.append('No Metacritic score')
    else:
        imdb_info.append(meta_score.get_text().strip())

    imdb_score = soup.find('span', {'itemprop': 'ratingValue'})
    imdb_info.append(imdb_score.get_text())

    imdb_votes = soup.find('span', {'itemprop': 'ratingCount'})
    imdb_info.append(imdb_votes.get_text())

    try:
        popularity = soup.findAll('span', {'class': 'subText'})
        imdb_info.append(popularity[2].get_text().strip().split(' ', 1)[0].strip())
    except IndexError:
        imdb_info.append('No popularity')

    page_json = soup.find('script', {'type': 'application/ld+json'})
    page_json = json.loads(page_json.get_text())

    try:
        imdb_info.append(page_json['contentRating'])
    except KeyError:
        imdb_info.append('No content rating')

    try:
        director = []
        for x in page_json['director']:
            if x['@type'] == 'Person':
                director.append(x['name'])
    except TypeError:
        director = page_json['director']['name']

    print()

    try:
        creator = []
        for x in page_json['creator']:
            if x['@type'] == 'Person':
                creator.append(x['name'])
    except TypeError:
        creator = page_json['creator']['name']

    print()

    try:
        actor = []
        for x in page_json['actor']:
            if x['@type'] == 'Person':
                actor.append(x['name'])
    except TypeError:
        actor = page_json['actor']['name']

    imdb_info.append(director)
    imdb_info.append(creator)
    imdb_info.append(actor)

    return imdb_info