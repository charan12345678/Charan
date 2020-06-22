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
        all_items = response.css('div.s-latency-cf-section')
        for i in all_items:
         product_name = i.css('.a-color-base.a-text-normal::text').extract()
         price = i.css('.a-price-whole').css('::text').extract()
         rating = i.css('.aok-align-bottom').css('::text').extract()

         items['product_name'] = product_name
         items['price'] = price
         items['rating'] = rating
            
         yield items
         

        next_page = 'https://www.amazon.in/s?k=phones&page='+ str(QuoteSpider.page_number) +'&qid=1592587195&ref=sr_pg_2'
        if QuoteSpider.page_number<=50:
           QuoteSpider.page_number +=1
           yield response.follow(next_page, callback = self.parse)
            