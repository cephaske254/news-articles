import urllib.request,json
from .models import NewsSourceModel,NewsArticleModel

api_key=None
base_url=None

def request_config(app):
    global api_key,base_url
    api_key = app.config['API_KEY']
    base_url = app.config['BASE_URL']
    # &q={query}&country={country}&sources={source}
def get_news_articles(endpoint,query,maximum):
    '''
    function that gets the json response from newsapi
    '''
    news_articles_url=base_url.format(endpoint,api_key,query)
    with urllib.request.urlopen(news_articles_url) as url:
        news_articles_data = url.read()
        news_articles_response = json.loads(news_articles_data)
        
        news_articles_results = None

        if(news_articles_response):
            news_articles_list = news_articles_response['articles']
            news_articles_results = process_results(news_articles_list,maximum)
    return news_articles_results

def process_results(news_articles_list,maximum):
    '''
    function that processes the revieved data
    '''
    results = [] 
    i=0
    for news in news_articles_list:
        source = news.get('source') 
        author = news.get('author') 
        title = news.get('title')
        description = news.get('description')
        url = news.get('url')
        urlToImage = news.get('urlToImage')
        publishedAt = news.get('publishedAt')
        content = news.get('content')
        i+=1
        if i <= maximum:
            if(urlToImage == None):
                urlToImage = 'static/images/default_news_image.png'
            news_object = NewsArticleModel(source,author,title,description,url,urlToImage,publishedAt,content)
            if content != None:
                results.append(news_object)
    return results


def get_sources(maximum):
    sources_url = base_url.format('sources',api_key,'')

    with urllib.request.urlopen(sources_url) as url:
        sources_response = json.loads(url.read())
        
        sources_results = None

        if sources_response:
            sources_list = sources_response['sources']
            sources_results = process_sources(sources_list,maximum)
    return sources_results

def process_sources(sources_list,maximum):
    '''
    function to generate a python dictionary containing sources
    '''
    sources=[]
    i=0
    for source in sources_list:
        i+=1
        if i <= maximum:
            id=source.get('id')
            name=source.get('name')
            description=source.get('description')
            url=source.get('url')
            category=source.get('category')
            language=source.get('language')
            country=source.get('country')

            source_object = NewsSourceModel(id,name,description,url,category,language,country)
            sources.append(source_object)
    return sources

