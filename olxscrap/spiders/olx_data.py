import scrapy
from olxscrap.items import OlxscrapItem

class OlxDataSpider(scrapy.Spider):
    name = 'olx_data'
    allowed_domains = ['https://www.olx.in/']
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723/']

    def parse(self, response):
        
        property_name=response.xpath("//*[@id='container/main/div/div/div/div[5]/div[1]/div/section/h1']/text()").extract()
        property_id=response.xpath("//*[@id='container/main/div/div/div/div[5]/div[5]/strong']/text()").extract()
        breadcrumbs=response.xpath("//*[@id='container/main/div/div/div/div[1]/div/ol']/text()").extract()
        price=response.xpath("//*[@id='container/main/div/div/div/div[5]/div[1]/div/section/span[1]']/text()").extract()
        image_url=response.xpath("//*[@id='container/main/div/div/div/div[4]/div/div/div[1]/div/div/div/div/div/div/div/figure/img']/text()").extract()
        description=response.xpath("//*[@id='container/main/div/div/div/div[4]/section[1]/div/div/div[2]/p']/text()").extract()
        seller_name=response.xpath("//*[@id='container/main/div/div/div/div[5]/div[2]/div/div/div[2]/div/a/div)']/text()").extract()
        location=response.xpath("//*[@id='container/main/div/div/div/div[5]/div[4]/div/div[1]/span']/text()").extract()
        property_type=response.xpath("//*[@id='container/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[1]/div/span[2]']/text()").extract()
        bathrooms=response.xpath("//*[@id='container/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[3]/div/span[2]']/text()").extract()
        bedrooms=response.xpath("//*[@id='container/main/div/div/div/div[4]/section[1]/div/div/div[1]/div/div[2]/div/span[2]']/text()").extract()
        
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
        
        
    
        
           
            
            
        
              
      
