import scrapy
#from ..items import QuotetutorialItem 
from quotetutorial.items import QuotetutorialItem


class QuoteSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
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

        next_page = 'https://www.amazon.in/s?k=phones&page='+ str(QuoteSpider.page_number) +'&qid=1592587195&ref=sr_pg_2'
        if QuoteSpider.page_number<=100:
            QuoteSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse)
            