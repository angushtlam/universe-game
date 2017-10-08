import requests


def get_random_article_id():
    r = requests.get('https://en.wikipedia.org/w/api.php?action=query&format=json&uselang=en&list=random&rnnamespace=0&rnlimit=1')
    return r.json()['query']['random'][0]['id']


def get_url_by_article_id(article_id):
    return 'https://en.wikipedia.org/?curid=' + str(article_id)


def get_article_title_by_article_id(article_id):
    r = requests.get('https://en.wikipedia.org/w/api.php?action=query&format=json&prop=info&pageids=' + str(article_id) + '&inprop=url')
    return r.json()['query']['pages'][str(article_id)]['title']


# def get_article_links_on_article_by_id(article_id):
#     r = requests.get('https://en.wikipedia.org/w/api.php?action=query&format=json&pageids=' + str(article_id) + '&generator=links&gpllimit=max')
#     print(r.json())
#     return r.json()['query']['pages'].keys()
