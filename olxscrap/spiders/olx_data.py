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
        all_urls = response.xpath(".//*[@data-aut-id='itemsList']/@href")
        for urls in all_urls:
            items_urls = urls.xpath(".//a[@class='fhlkh']/@href").get()
            yield response.follow(url=items_urls, callback=self.parse)
      
            loader = ItemLoader(item=OlxscrapItem(),selector=urls,response=response)
            loader.add_xpath("property_name",".//*[@data-aut-id='itemTitle']/text()")
            loader.add_xpath("property_id",".//*[@class='container']/main/div/div/div/div[5]/div[5]/strong/text()")
            loader.add_xpath("breadcrumbs",".//*[@data-aut-id='breadcrumb']/text()")
            loader.add_xpath("price",".//*[@data-aut-id='itemPrice']/text()")
            loader.add_xpath("image_url",".//a[@data-aut-id='defaultImg']/@href")
            loader.add_xpath("description",".//*[@data-aut-id='itemDescriptionContent']/text()")
            loader.add_xpath("seller_name",".//*[@class='container']/main/div/div/div/div[5]/div[2]/div/div/div[2]/div/text()")
            loader.add_xpath("location",".//*[@data-aut-id='itemLocation']/text()")
            loader.add_xpath("property_type",".//*[@data-aut-id='value_type']/text()")
            loader.add_xpath("bathrooms",".//*[@data-aut-id='value_bathrooms']/text()")
            loader.add_xpath("bedrooms",".//*[@data-aut-id='value_rooms']/text()")
            yield loader.load_item()
                             
        load_more = response.xpath("//*[@data-aut-id='btnLoadMore']").get()
        if load_more:
            yield response.follow(url=load_more, callback=self.parse)
    
     
    
        
        
        
        
        
    
        
           
            
            
        
              
      
