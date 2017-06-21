"""
This module provides a google news search API.
"""

class GoogleNewsRetrievalException(Exception):
    pass



class GoogleNews(object):
    

    def __init__(self, query_string):
        
        self.query_string = query_string.replace(" ", "+")
        self.page = None
    
    def links(self):
        pass
    
    
    def build(self):
        url_template = "https://www.google.es/search?q={}&tbm=nws"
        url = url_template.format(self.query_string)
        self.page = requests.get(url)
        return self.page
    
    def __str__(self):
        if self.page is None:
            return self.page
        
    
    
    


