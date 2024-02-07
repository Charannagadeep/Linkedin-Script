import scrapy
from linked.items import LinkedInProfileItem

class LinkedInSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["linkedin.com"]

    def start_requests(self):
        search_url = "https://www.linkedin.com/search/results/people/?keywords=firstname%20lastname&origin=SWITCH_SEARCH_VERTICAL&searchId=56c27c50-e74d-4895-ada0-bf3fe66b0ea0&sid=5W!"
        yield scrapy.Request(url=search_url, callback=self.parse)

    def parse(self, response):
        profiles = response.css('.reusable-search__result-container')

        for profile in profiles:
            item = LinkedInProfileItem()
            item['name'] = profile.css('.entity-result__title-text a::text').get()
            item['info'] = profile.css('.entity-result__primary-subtitle::text').get()
            item['place'] = profile.css('.entity-result__secondary-subtitle::text').get()

            #extracted data
            print("Name:", item['name'])
            print("Info:", item['info'])
            print("Place:", item['place'])
            print("\n")

            # CSV 
            yield item
