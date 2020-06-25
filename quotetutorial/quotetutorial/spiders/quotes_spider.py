import scrapy
#from ..items import QuotetutorialItem 
from quotetutorial.items import QuotetutorialItem 
import re


class QuoteSpider(scrapy.Spider):
    name = 'amazon'
    page_number = 2
    start_urls = [
        'https://www.amazon.in/s?k=phones&ref=nb_sb_noss_2'
        
    ]

    def parse(self,response):
        #items = QuotetutorialItem()
        all_items = response.css('div.s-latency-cf-section')
        for i in all_items:
         #product_name = i.css('.a-color-base.a-text-normal::text').extract()
         #price = i.css('.a-price-whole').css('::text').extract()
         #rating = i.css('.aok-align-bottom').css('::text').extract()
         hrefs = i.css('.a-text-normal::attr(href)').extract_first()

         #items['product_name'] = product_name
         #items['price'] = price
         #items['rating'] = rating
         #items['hrefs'] = hrefs 

         if hrefs is not None:
             yield response.follow(hrefs,callback =self.parse_page)  
                
         #yield items
            
    #def parse_config(self, response):
     #   for href in response.css(".a-text-normal::attr(href)"):
      #      url = response.urljoin(href.extract_first())
       #     yield scrapy.Request(url, callback = self.parse_page)

    def parse_page(self, response):
        items = QuotetutorialItem()
        #news = Newclass()
        #labels = response.css('.col1 .label::text').extract()
        values = response.css('.col1 .value::text').extract()
        product_name = response.css('#productTitle::text').extract_first().strip()
        price = response.css('#priceblock_ourprice::text').extract_first().strip() 


            
            
        #rating = response.css('.a-star').css('::text').extract_first().strip()

        #items['labels'] = labels
        items['values'] = values
        items['product_name'] = product_name
        items['price'] = price
        #items['rating'] = rating

        items['OS'] = items['values'][0]
        items['RAM'] = items['values'][1]
        items['Item_weight'] = items['values'][2]
        items['Product_Dimensions'] = items['values'][3]
        items['Item_model'] = items['values'][4]
        items['Wireless'] = items['values'][5]
        items['connectivity'] = items['values'][6]
        items['special_features'] = items['values'][7]
        items['Display_technology'] = items['values'][8]
        items['other_camera_features'] = items['values'][9]
        items['form_factor'] = items['values'][10]
        items['Battery_Power_Rating'] = items['values'][11]

        yield items

        
            #print(items['labels'][i] +'::: '+ items['values'][i])
        
        

    

       # next_page = 'https://www.amazon.in/s?k=phones&page='+ str(QuoteSpider.page_number) +'&qid=1592587195&ref=sr_pg_2'
        #if QuoteSpider.page_number<=50:
         #  QuoteSpider.page_number +=1
          # yield response.follow(next_page, callback = self.parse)
        
            