# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import (TakeFirst, 
                                      MapCompose, 
                                      Join)
from w3lib.html import remove_tags
import re


def remove_html(review_summary):
    review = ''
    try:
        review = remove_tags(review_summary)
    except TypeError:
        review = 'No Reviews'
        
    cleaned_review_summary = re.sub('(\d{1,2}%)', r' - \1', review)
    return cleaned_review_summary

def get_platforms(one_class):
    platforms = []
    
    platform = one_class.split(' ')[-1]
    if platform == 'win':
        platforms.append('Windows')
    if platform == 'mac':
        platforms.append('Mac OS')
    if platform == 'linux':
        platforms.append('Linux')
    if platform == 'vr_supported':
        platforms.append('VR Supported')
            
    return platforms

def get_original_price(original_price):
    return original_price.strip()

def clean_discount_rate(discount_rate):
    if discount_rate:
        return discount_rate.lstrip('-')
        
    return discount_rate

def clean_discounted_price(discounted_price):
    if discounted_price:
        return discounted_price.strip()
    return discounted_price

class SteamStoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    img_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    game_name = scrapy.Field(
        output_processor = TakeFirst()
    )
    release_date = scrapy.Field(
        output_processor = TakeFirst()
    )
    platforms = scrapy.Field(
        input_processor = MapCompose(get_platforms)
    )
    reviews_summary = scrapy.Field(
        input_processor = MapCompose(remove_html),
        output_processor = TakeFirst()
    )
    discount_rate = scrapy.Field(
        input_processor = MapCompose(clean_discount_rate),
        output_processor = TakeFirst()
    )
    original_price = scrapy.Field(
        input_processor = MapCompose(get_original_price),
        output_processor = TakeFirst()
    )
    discounted_price = scrapy.Field(
        input_processor = MapCompose(clean_discounted_price),
        output_processor = TakeFirst()
    )
