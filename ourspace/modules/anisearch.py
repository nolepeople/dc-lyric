
import lk21.extractors as ex
from . import ListToString

class Anime:

    def __init__(self):
        pass


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


        

