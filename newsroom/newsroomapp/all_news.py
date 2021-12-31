import requests

def all_news():
    # url = "https://indian-news-live.p.rapidapi.com/news"
    #
    # headers = {
    #     'x-rapidapi-host': "indian-news-live.p.rapidapi.com",
    #     'x-rapidapi-key': "34262c539amsh117b337c7ab904fp198546jsn3cb7619c8fb4"
    # }
    #
    # response = requests.request("GET", url, headers=headers)
    #
    # return response.json()
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=in&'
           'apiKey=e239ae2c024f47158fb32f48420830c7')
    response = requests.get(url)
    return response.json()['articles']

# print(all_news())