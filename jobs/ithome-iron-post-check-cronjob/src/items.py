# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IthomeContentInfoItem(scrapy.Item):
    """ithome content data"""
    title = scrapy.Field()
    like = scrapy.Field()
    comment = scrapy.Field()
    view = scrapy.Field()
    create_datetime = scrapy.Field()
