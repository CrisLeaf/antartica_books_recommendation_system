import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
from data_scraper.utils import replace_iso, remove_spaces, replace_uper, clean_price, \
                               clean_discount, fill_na_string, fill_na_float, clean_text

class BooksScraperItem(scrapy.Item):
    name = scrapy.Field(input_processor=MapCompose(
        remove_tags, replace_uper, replace_iso, remove_spaces, clean_text
    ), output_processor=TakeFirst())
    author = scrapy.Field(input_processor=MapCompose(
        remove_tags, replace_uper, replace_iso, remove_spaces, clean_text
    ), output_processor=TakeFirst())
    editorial = scrapy.Field(input_processor=MapCompose(
        remove_tags, replace_uper, replace_iso, remove_spaces, clean_text
    ), output_processor=TakeFirst())
    price = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_spaces, clean_price
    ), output_processor=TakeFirst())
    discount = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_spaces, clean_discount
    ), output_processor=TakeFirst())
    category = scrapy.Field(input_processor=MapCompose(
        remove_tags, replace_uper, replace_iso, remove_spaces, clean_text
    ), output_processor=TakeFirst())
    language = scrapy.Field(input_processor=MapCompose(
        remove_tags, replace_uper, replace_iso, remove_spaces, clean_text
    ), output_processor=TakeFirst())
    pages = scrapy.Field(input_processor=MapCompose(
        remove_tags, remove_spaces, clean_price
    ), output_processor=TakeFirst())
    review = scrapy.Field(input_processor=MapCompose( 
        remove_tags, replace_uper, replace_iso, remove_spaces, clean_text
    ), output_processor=TakeFirst())
    link = scrapy.Field(input_processor=MapCompose(), output_processor=TakeFirst())