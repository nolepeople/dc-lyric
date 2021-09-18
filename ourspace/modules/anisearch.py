import lk21.extractors as ex
from .helper import Helper

class Anime:

    def __init__(self,query,server):
        self.query = query
        self.server = server

    def result(self):
        if self.server.lower() not in [web for web in self.website().split('\n')]:
            return "return await ctx.send('server not found')"

        self.scraper = \
            eval('ex.{}.{}()'.format(self.server,self.server.capitalize()))

        self.infoRes = self.scraper.search(self.query)
        self.titles = [title['title'] for title in self.scraper.search(self.query)]

        if self.titles:
           return Helper.ListToString(self.titles)
        return {'status':None,'info':"sorry result not found :("}

    def extract_urls(self,ID):
        self.meta = self.scraper.extract(self.infoRes[ID])
        self.image = self.meta['metadata']['image']
        return self.meta['download']


    @staticmethod
    def website():
        ListS = list(ex.__dict__)[24:]

        extendsList = [
                'layarkaca21',
                'nekopoi',
                'bbcsjav',
                'kdramaindo',
                'bypasser',
                'dramaindo',
                'melongmovie',
                ]

        for serverName in ListS:
            if serverName in extendsList:
                ListS.remove(serverName)

        #idk men bypasser,melongmovie not detect in ListS so i remove this value again
        ListS.remove('bypasser')
        ListS.remove('melongmovie')
        return """```
{}
```""".format('\n'.join(ListS))


if __name__=="__main__":
    a = Anime('tokyo','wibudesu')
    a.result()
    print (a.infoRes[1])
    print (a.extract_urls(0))

