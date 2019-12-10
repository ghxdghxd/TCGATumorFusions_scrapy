# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TumorfusionsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Cancer = scrapy.Field()
    TCGA_sampleID = scrapy.Field()
    FusionPair = scrapy.Field()
    E_value = scrapy.Field()
    Tier = scrapy.Field()
    Frame = scrapy.Field()
    phosphorylation = scrapy.Field()
    ubiquitination = scrapy.Field()
    WGS = scrapy.Field()
