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
        for region in response.css('table.sortable'):
            school = self.parse_school(region)
            yield {'region': school}

    def parse_school(self, region):
        school_list = []
        for school in region.css('tr'):
          school_list.append({
            'name': school.css('td:nth-child(1) a::text, td:nth-child(1)::text').extract_first(),
            'location': school.css('td:nth-child(2) a::text, td:nth-child(2)::text').extract_first(),
            'country': school.css('td:nth-child(3) a::text, td:nth-child(3)::text').extract_first(),
            'control': school.css('td:nth-child(4) a::text, td:nth-child(4)::text').extract_first(),
            'type': school.css('td:nth-child(5) a::text, td:nth-child(5)::text').extract_first(),
            'enrollment': school.css('td:nth-child(6) a::text, td:nth-child(6)::text').extract_first(),
            'founded': school.css('td:nth-child(7) a::text, td:nth-child(7)::text').extract_first(),
            'cilect': school.css('td:nth-child(8) a::text, td:nth-child(8)::text').extract_first(),
          })
        return school_list