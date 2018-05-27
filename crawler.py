import requests
from bs4 import BeautifulSoup


class Content:
    """
    Common base class for all articles/pages
    """

    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        """
        Flexible printing function controls output
        """
        print("New article found for topi:{}".format(self.topic))
        print('Title:{}'.format(self.title))
        print('URL:{}'.format(self.url))
        print('Body:{}\n'.format(self.body))

    def getPage(url):
        req = requests.get(url)
        return BeautifulSoup(req.text, 'html.parser')

    def scraeNYTimes(url):
        bs = getPage(url)
        title = bs.find("h1").text
        lines = bs.find_all("p", {"class": "story-content"})
        body = '\n'.join([line.text for line in lines])
        return Content(url, title, body)

    def scrapeBrookings(url):
        bs = getPage(url)
        title = bs.find_all("h1").text
        body = bs.find("div", {"class": "post-body"}).text
        return Content(url, title, body)


class Website:
    """
    Contains information about website structure
    """

    def __init__(self, name, url, searchResult, resultListing, resultUrl, absolueUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absolueUrl = absolueUrl
        self.titleTage = titleTag
        self.bodyTag = bodyTag

    url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths'
    content = scrapeNYTimes(url)
    print('Title:{}'.format(content.title))
    print('URL:{}\n'.format(content.url))
    print(content.body)
