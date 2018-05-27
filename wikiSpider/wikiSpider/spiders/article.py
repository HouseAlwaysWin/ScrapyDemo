import scrapy


class ArticleSpider(scrapy.Spider):
    name = 'article'

    def start_request(self):
        urls = [
            'http://en.wikipedia.org/wiki/Functional_programming',
            'http://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url, callback=self.parse)]

    def parse(self.response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('URL is: {}'.format(url))
        print('TItle is: {}'.format(title))
