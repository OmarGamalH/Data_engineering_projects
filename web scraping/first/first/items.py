# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

def remove_currency_serilizer(value : str):
        if value.startswith("£"):
            return float(value.replace("£" , ""))
        else:
             return float(value)
def availibity_serializer(value : str):
    number = ""
    if "In stock" in value:
        for char in value:
            if char.isdigit():
                number += str(char)
    else:
         return value
    return int(number)


class Book(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field(serializer = remove_currency_serilizer)
    UPC = scrapy.Field()
    product_type = scrapy.Field()
    price_excl = scrapy.Field(serializer = remove_currency_serilizer)
    price_incl = scrapy.Field(serializer = remove_currency_serilizer)
    tax = scrapy.Field(serializer = remove_currency_serilizer)
    availability = scrapy.Field(serializer = availibity_serializer)
    reviews = scrapy.Field()


