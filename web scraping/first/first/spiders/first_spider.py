import scrapy
from ..items import Book

class First_Spider(scrapy.Spider):
    name = "first_spider"
    allowed_domains = ["books.toscrape.com" , "books.toscrape.comcatalogue"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self , response):
        books =  response.css("article.product_pod")

        for book in books:
            if "catalogue" in response.url:
                missing = "catalogue/"
            else:
                missing = ""
            book_url = "https://books.toscrape.com/" + missing +  book.xpath(".//div[@class = 'image_container']/a/@href").get()
            yield response.follow(book_url , callback = self.parse_book)
            

        next_url = response.css('li.next a::attr(href)').get()
        if next_url is not None:
           yield response.follow(next_url , callback = self.parse)

    def parse_book(self , response):
        book = Book()
        book["name"]= response.xpath("//article[@class = 'product_page']/div[@class = 'row']/div[2]/h1/text()").get()
        book["price"] = response.xpath("//article[@class = 'product_page']/div[@class = 'row']/div[2]/p[1]/text()").get()
        keys = response.css("th::text").getall()
        values = response.css("td::text").getall()
        book["UPC"] = values[0]
        book["product_type"] = values[1]
        book["price_excl"] = values[2]
        book["price_incl"] = values[3]
        book["tax"] = values[4]
        book["availability"] = values[5]
        book["reviews"] = values[6]
    

        yield book