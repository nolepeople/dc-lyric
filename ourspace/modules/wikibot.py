import wikipedia
from .helper import *

class wiki:

    def __init__(self,query,lang):
        self.wikipedia = wikipedia
        self.wikipedia.set_lang(lang)
        self.query = query
        self.lang = lang

    def search_result(self):
        self.result = self.wikipedia.search(self.query)

        if self.result:
           return ListToString(self.result)

        return {'status':None,'info':'Sorry result not found :('}

    def summary(self,keyword):
        self.keyword = keyword
        return f"""```
{self.wikipedia.summary(self.keyword,sentences=1)}
```"""
