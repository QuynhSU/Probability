import scrapy

class CrawlerItem(scrapy.Item):
    User = scrapy.Field()
    Comment = scrapy.Field()
    Time = scrapy.Field()
