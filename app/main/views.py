from flask import render_template,redirect,url_for,request
from . import main
from ..requests import get_news_articles,get_sources

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
    
    query = request.args.get('query')
    if query:
        return redirect(url_for('main.search',keywords = query))
    else:
        return render_template('index.html',title='Home | News General',general=general,science=science,technology=technology,health=health,entertainment=entertainment,business=business)

@main.route('/search/<keywords>')
def search(keywords):
    '''
    View function to display the search results
    '''
    search_keywords = '+'.join( keywords.split(' '))
    search_results = get_news_articles('everything',f'q={search_keywords}',100)

    query = request.args.get('query')
    if query:
        return redirect(url_for('main.search',keywords = query))
    else:
        return render_template('search.html',results = search_results, title=f'Search Results for {keywords}')


@main.route('/categories/<category_name>')
def categoies(category_name):
    '''
    function that renders the categories.html to display news according to the category which the user chose
    '''
    category = get_news_articles('top-headlines',f'category={category_name}',100)

    query = request.args.get('query')
    if query:
        return redirect(url_for('main.search',keywords = query))
    else:
        return render_template('categories.html',category=category, title = f'Categories | {category_name}',category_name=category_name)


@main.route('/sources')
@main.route('/sources/<source_name>')
def sources(source_name=None):
    '''
    function that renders the sources page
    '''
    sources = get_sources(1000000)
    from_source = get_news_articles('top-headlines',f'sources={source_name}',100)

    query = request.args.get('query')
    if source_name:
        return render_template('sources.html',source_name = source_name,title=f'Sources | {source_name}',from_source=from_source)
    elif query:
        return redirect(url_for('main.search',keywords = query))
    else:
        return render_template('sources.html',title='Sources | All',sources=sources)


