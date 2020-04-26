from flask import render_template
from . import main
from ..requests import get_news_articles
from .forms import SearchForm

#Views 
@main.route('/',methods = ['GET','POST'])
def index():
    searchForm = SearchForm()
    general = get_news_articles('top-headlines','category=general',4)
    science = get_news_articles('top-headlines','category=science',4)
    technology = get_news_articles('top-headlines','category=technology',4)
    health = get_news_articles('top-headlines','category=health',4)
    # health = get_news_articles('top-headlines','category=business',4)
    entertainment = get_news_articles('top-headlines','category=entertainment',4)
    business = get_news_articles('top-headlines','category=business',4)
    return render_template('index.html',title='Home | News General',general=general,science=science,technology=technology,health=health,entertainment=entertainment,business=business,search_form=searchForm)