class NewsSourceModel:
    '''
    class for the structure of the expected news structure from api
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class NewsArticleModel:
    def __init__(self,source,source_id,author,title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.source_id = source_id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content