import requests
import re,sys
from bs4 import BeautifulSoup


class find:
    url = "https://search.azlyrics.com/search.php?q="
    more = '<span class="glyphicon glyphicon-zoom-in"></span> More Song Results</a>'

    def __init__(self,query):
        self.q = query
        self.req = requests.get("{}{}".format(self.url,self.q)).text

    def result(self):
        self.default_r = re.findall(r"\s{1,}\d{1,}\..*?\s(.*?)\s{1,}</td>",self.req)
        self.list = []
        for hi in self.default_r:
            if "/h/" not in hi:
               if "/f/" not in hi:
                  try:
                      self.urlsp = re.findall(r'\shref="(.*)">',hi)[0]
                      self.title = re.sub(r'<a(.*?)>|<.*?>|(\s\s)',"",hi).replace('"','')
                      self.list.append({"title":self.title,"url":self.urlsp})
                  except IndexError:
                      pass
        if len(self.list) <= 1:
            return None
        return self.list

    def results(self):
        self.list = self.result()
        self.pattern = 'href="\?(.*?)"'
        if str(self.more) in self.req:
            self.npage = re.findall(self.pattern,self.req)
            self.url = "{}{}".format(
                    self.url,
                    self.npage[0].replace("q=","")
                    )

            self.req = requests.get(self.url).text
            self.results=re.findall(r"\s{1,}\d{1,}\..*?\s(.*?)\s{1,}</td>",self.req)
            self.list = []
            for _ in self.results:
                if "/h/" not in _:
                    if "/f/" not in _:
                        try:
                            if _ not in self.list:
                                self.urlsp = re.findall(r'\shref="(.*)">',_)[0]
                                self.title = re.sub(r'<a(.*?)>|<.*?>|(\s\s)',"",_)
                                self.list.append({"title":self.title.replace(
                                    '"',""
                                    ),"url":self.urlsp})
                        except IndexError:
                            pass
            return self.list
        return self.list


class get:

    def __init__(self,u):
        self.req = requests.get(u).text

    def lyric(self):
        self.soup = BeautifulSoup(self.req,"html.parser")
        self.lyr = """
"""
        for _ in [div.text for div in self.soup.find_all("div",{"class":None})]:
           self.lyr += _

        if len(self.lyr) <= 1:
           return None
        return self.lyr
