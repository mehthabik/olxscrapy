import scrapy
from ..items import OlxscrapItem

class OlxDataSpider(scrapy.Spider):
    name = 'olx_data'
    allowed_domains = ['https://www.olx.in/']
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723']

    def parse(self, response):
        
        items=OlxscrapItem()
        property_name=response.css('._2tW1I::text').extract()
        property_id=response.css('strong::text').extract()
        breadcrumbs=response.css('.rui-10Yqz::text').extract()
        price=response.css('._2xKfz::text').extract()
        image_url=response.css('._39P4_:att:(src)').extract()
        description=response.css('p::text').extract()
        seller_name=response.css('._3oOe9::text').extract()
        location=response.css('._2FRXm::text').extract()
        property_type=response.css('._2vNpt::text').extract()
        bathrooms=response.css('._2vNpt::text').extract()
        bedrooms=response.css('._2vNpt::text').extract()
        
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
        
              
      
