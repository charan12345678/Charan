import scrapy
#from ..items import QuotetutorialItem 
from quotetutorial.items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.in/s?k=phones&ref=nb_sb_noss_2'
    ]

    def parse(self,response):
        items = QuotetutorialItem()

        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        price = response.css('.a-price-whole').css('::text').extract()
        rating = response.css('.aok-align-bottom').css('::text').extract()

        items['product_name'] = product_name
        items['price'] = price
        items['rating'] = rating
            
        yield items
            