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
          for school in response.xpath('//table/tr'):
              yield {
                  'school': school.xpath('td[1]/a/text()'),
                  'location': school.xpath('td[2]/text()'),
                  'country': school.xpath('td[3]/text()'),
                  'control': school.xpath('td[4]/text()'),
                  'type': school.xpath('td[5]/text()'),
                  'enrollment': school.xpath('td[6]/text()'),
                  'founded': school.xpath('td[7]/text()'),
                  'cilect': school.xpath('td[8]/text()'),
              }           