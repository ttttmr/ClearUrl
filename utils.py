# from newspaper import Article
import requests

def get_url_content(url):
    # article = Article(url)
    resp = requests.get(url)
    return resp.content