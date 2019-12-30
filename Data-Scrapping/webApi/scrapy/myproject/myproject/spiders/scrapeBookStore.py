import scrapy

class Bookstore(scrapy.Spider):
    name="bookStore"
    def start_requests(self):
        url="http://books.toscrape.com/"
        yield scrapy.Request(url=url,callback=self.parse)
        
    def parse(self,response):
        filename="bookstore.html"
        
        for l in response.css("ol.row li"):
            article=l.css("article.product_pod")
            title=article.css("h3")
            tit=title.css("a::attr(title)").get()
            img=article.css("img::attr(src)").get()
            price=article.css("p.price_color::text").get()
            
            yield {
                "image_url":img,
                "book_title":tit,
                "product_price":price
            }
        
        
        next_page=response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page=response.urljoin(next_page)
            yield scrapy.Request(next_page,callback=self.parse)
            