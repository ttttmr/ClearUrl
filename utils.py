from newspaper import Article

def get_url_content(url):
    article = Article(url)
    return article.text