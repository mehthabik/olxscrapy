import scrapy
from olxscrap.items import OlxscrapItem


class OlxDataSpider(scrapy.Spider):
    name = 'olx_data'
    allowed_domains = ['www.olx.in']
    start_urls = ['https://www.olx.in/kozhikode_g4058877/for-rent-houses-apartments_c1723/']
    
    def parse(self, response):
        for link in response.css('li.EIR5N a::attr(href)'):
            yield response.follow(link.get(),callback=self.parse_categories)
    
    def parse_categories(self,response):
        property_name = response.css('h1._3rJ6e::text').get()
        property_id = response.css('strong::text').extract()[2]
        breadcrumbs = response.css('._3C_pO::text').getall()
        price = response.css('span._2xKfz::text').get()
        image_url = response.css("img._39P4_::attr(src)").get()
        description =  response.css("p::text").get()
        seller_name = response.css("._3oOe9::text").get()
        location = response.css("._2FRXm::text").get()
        property_type = response.css("._2vNpt::text").get()
        bathrooms= response.css("._2vNpt::text").extract()[2]
        bedrooms = response.css("._2vNpt::text").extract()[1]
        
        yield{
            'property_name':property_name,
            'property_id'  :property_id,
            'breadcrumbs'  :breadcrumbs,
            'price'        :price,
            'image_url'    :image_url,
            'description'  :description,
            'seller_name'  :seller_name,
            'location'     :location,
            'property_type':property_type,
            'bathrooms'    :bathrooms,
            'bedrooms'     :bedrooms,
            
        }
        
        
        
        
            
      
            
            
    
     
    
        
        
        
        
        
    
        
           
            
            
        
              
      
