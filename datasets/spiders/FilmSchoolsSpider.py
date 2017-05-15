import scrapy


class FilmSchoolsSpider(scrapy.Spider):
    name = "FilmSchools"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/List_of_film_schools',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'FilmSchools-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)