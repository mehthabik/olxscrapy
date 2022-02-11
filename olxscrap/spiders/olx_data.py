import scrapy
from olxscrap.items import OlxscrapItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider,Rule

class OlxDataSpider(scrapy.Spider):
    name = 'olx_data'
    allowed_domains = ['olx.com']
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723/']
    
    olx_links=LinkExtractor(restrict_css='.fhlkh')
    olx_next=LinkExtractor(restrict_css='.rui-1JPTg')
    
    olx_rule=Rule(olx_links,callback='parse_item',follow=False)
    rule_next=Rule(olx_next,follow=True)
    
    rules=(
        olx_rule,rule_next
    )
        

    def parse(self, response):
        property_name=response.css('._3rJ6e::text').get()
        property_id=response.css('strong::text').get()
        breadcrumbs=response.css('.rui-10Yqz::text').get()
        price=response.css('._2xKfz::text').get()
        image_url=response.css('.UYvAv::text').get()
        description=response.css('p::text').get()
        seller_name=response.css('._1oSdP::text').get()
        location=response.css('._2A3Wa::text').get()
        property_type=response.css('._3_knn:nth-child(1) ._2vNpt::text').get()
        bathrooms=response.css('._3_knn:nth-child(3) ._2vNpt::text').get()
        bedrooms=response.css('._3_knn:nth-child(2) ._2vNpt::text').get()
        
        items=OlxscrapItem()        
        items['property_name']=property_name
        items['property_id']=property_id
        items['breadcrumbs']=breadcrumbs
        items['price']=price
        items['image_url']=image_url
        items['description']=description
        items['seller_name']=seller_name
        items['location']=location
        items['property_type']=property_type
        items['bathrooms']=bathrooms
        items['bedrooms']=bedrooms
        
        yield items
             
        
        
        
        
        
        
    
        
           
            
            
        
              
      
