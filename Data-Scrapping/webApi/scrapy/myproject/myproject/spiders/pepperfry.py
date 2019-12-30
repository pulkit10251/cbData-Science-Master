import scrapy
import os

class pepperfry(scrapy.Spider):
    name="pepperFry"
    Base_dir='./Peperfry_data/'
    max_cnt=20
    
    def start_requests(self):
        
        base_URL="https://www.pepperfry.com/site_product/search?q="
        items=["two seater sofa","bench","book cases","coffee table","dining set","queen beds","arm chairs","chest drawers","garden seating","bean bags","king beds"]
        
        urls=[]
        dir_names=[]
        
        for item in items:
            query_string='+'.join(item.split(' '))
            dir_name='-'.join(item.split(' '))
            urls.append(base_URL+query_string)
            dir_path=self.Base_dir+dir_name
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
                
        for i in range(len(urls)):
            d={
                "dir_name":dir_names[i]
            }
            resp=scrapy.Request(url=url[i],callback=self.parse,dont_filter=True)
            resp.meta['dir_name']=dir_names[i]
            yield resp
            
            
    def parse(self,response,**meta):
        product_urls=response.xpath('//div/div/div/a[@p=0]/@href').extract()
        counter=0
        
        for url in product_urls:
            resp=scrapy.Request(url=url,callback=self.parse,dont_filter=True)
            resp.meta['dir_name']=response.meta['dir_name']
            
            if counter==self.max_cnt:
                break
                
            if not resp==None:
                counter+=1
                
        
        
        
        
        
        
        
        
        
        
        
        