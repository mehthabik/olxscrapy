import scrapy
from olxscrap.items import OlxscrapItem
from scrapy.loader import ItemLoader
from scrapy.crawler import CrawlerProcess

class OlxDataSpider(scrapy.Spider):
    name = 'olx_data'
    allowed_domains = ['www.olx.in']
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723/']
    
   
    def start_requests(self):
         yield scrapy.Request('https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723/', callback=self.parse)
    
    def parse(self, response):
        all_urls = response.xpath('//ul[@class="rl3f9 _3mXOU"]')
        for urls in all_urls:
            items_urls = urls.xpath(".//a[@class='fhlkh']/@href").get()
            yield response.follow(url=items_urls, callback=self.parse)
      
            loader = ItemLoader(item=OlxscrapItem(),selector=urls,response=response)
            loader.add_xpath("property_name",".//*[@class='container']/text()")
            loader.add_xpath("property_id",".//*[@class='container']/main/div/div/div/div[5]/div[5]/strong/text()")
            loader.add_xpath("breadcrumbs",".//*[@class='container']/main/div/div/div/div[1]/text()")
            loader.add_xpath("price",".//*[@class='container']/main/div/div/div/div[5]/div[1]/div/section/span[1]/text()")
            loader.add_xpath("image_url",".//a[@class='_2W83m']/@href")
            loader.add_xpath("description",".//*[@class='container']/main/div/div/div/div[4]/section[1]/div/div/div[2]/text()")
            loader.add_xpath("seller_name",".//*[@class='container']/main/div/div/div/div[5]/div[2]/div/div/div[2]/div/text()")
            loader.add_xpath("location",".//*[@class='container']/main/div/div/div/div[5]/div[1]/div/section/div/div[1]/div/span/text()")
            loader.add_xpath("property_type",".//*[@class='container']/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[1]/div/span[2]/text()")
            loader.add_xpath("bathrooms",".//*[@class='container']/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[3]/div/span[2]/text()")
            loader.add_xpath("bedrooms",".//*[@class='container']/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[2]/div/span[2]/text()")
            yield loader.load_item()
                             
        load_more = response.xpath("//a[@class='rui-39-wj rui-3evoE rui-1JPTg']/@href").get()
        if load_more:
            yield response.follow(url=load_more, callback=self.parse)
    
     
    
        
        
        
        
        
    
        
           
            
            
        
              
      
