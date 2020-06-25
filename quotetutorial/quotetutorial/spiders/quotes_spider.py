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
         hrefs = i.css('.a-text-normal::attr(href)').extract_first()

         items['product_name'] = product_name
         items['price'] = price
         items['rating'] = rating
         items['hrefs'] = hrefs
            
         yield items

    def parse_config(self, response):
        for href in response.css(".a-text-normal::attr(href)"):
            url = response.urljoin(href.extract_first())
            yield scrapy.Request(url, callback = self.parse_page)

    def parse_page(self, response):
        labels = response.css('.col1 .label::text').extract()
        values = response.css('.col1 .value::text').extract()
        scraped_info = {
           'labels' : labels,
            'values' : values
                }
        yield scraped_info
    

       # next_page = 'https://www.amazon.in/s?k=phones&page='+ str(QuoteSpider.page_number) +'&qid=1592587195&ref=sr_pg_2'
        #if QuoteSpider.page_number<=50:
         #  QuoteSpider.page_number +=1
          # yield response.follow(next_page, callback = self.parse)
        
            