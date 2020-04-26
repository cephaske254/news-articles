from flask import render_template,redirect,url_for,request
from . import main
from ..requests import get_news_articles

#Views 
@main.route('/',methods = ['GET','POST'])
def index():
    general = get_news_articles('top-headlines','category=general',4)
    science = get_news_articles('top-headlines','category=science',4)
    technology = get_news_articles('top-headlines','category=technology',4)
    health = get_news_articles('top-headlines','category=health',4)
    # health = get_news_articles('top-headlines','category=business',4)
    entertainment = get_news_articles('top-headlines','category=entertainment',4)
    business = get_news_articles('top-headlines','category=business',4)
    
    if(request.args.get('query')


    return render_template('index.html',title='Home | News General',general=general,science=science,technology=technology,health=health,entertainment=entertainment,business=business)

@main.route('/search/<keywords>')
def search(keywords):
    '''
    View function to display the search results
    '''
    search_keywords = '+'.join( keywords.split(' '))
    search_results = get_news_articles('everything',f'q={search_keywords}',100)
    return render_template('search.html',results = search_results)

