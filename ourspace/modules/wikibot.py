
import wikipedia 

class wiki:

    def __init__(self,query,lang="en"):
        if lang == "":
           lang = "en"

        self.wikipedia = wikipedia
        self.wikipedia.set_lang = lang
        self.query = query
        self.lang = lang

    def search_result(self):
        self.result = self.wikipedia.search(self.query)
        if self.result:

           self.Newlist = []
           self.index = 0

           for self.name in self.result:
               self.Newlist.append(f'{self.index}. {self.name}')
               self.index += 1

           self.output = '\n'.join(self.Newlist)
           return f"""```
{self.output}
```"""
        return {'status':None,'info':'Sorry result not found :('}
     


 
    def summary(self,keyword):
        self.keyword = keyword
        return self.wiki.summary(self.keyword)
