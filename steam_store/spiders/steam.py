import scrapy
from ..items import SteamStoreItem
from scrapy_playwright.page import PageMethod
from scrapy import Selector
from scrapy.loader import ItemLoader


class SteamSpider(scrapy.Spider):
    name = 'steam'
    
    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }
    
    # def clean_discount_price(self, discount_price):
    #     if discount_price:
    #         return discount_price[2].rstrip()
    #     return 'No Discount'
    
    def start_requests(self):
        yield scrapy.Request(
            url='https://store.steampowered.com/search/?filter=topsellers',
            meta={
                'playwright': True,
                'playwright_include_page': True,
                'playwright_page_methods': [
                    PageMethod("wait_for_selector", "div#search_resultsRows a")
                ]
            }
        )
    
    async def parse(self, response):
        page = response.meta['playwright_page']
        for i in range(2,3):
            games_count = 50 * i
            await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
            await page.wait_for_selector(f"div#search_resultsRows a:nth-child({games_count})")
        steam_html = await page.content()
        soup = Selector(text= steam_html)
        await page.close()
    
        games = soup.css('div#search_resultsRows > a')
        
        for game in games:
            loader = ItemLoader(item=SteamStoreItem(), selector=game, response=response)
            loader.add_css('game_url', '::attr(href)')
            loader.add_css('img_url', 'div.col.search_capsule img ::attr(src)')
            loader.add_css('game_name', '.responsive_search_name_combined span.title ::text')
            loader.add_css('release_date', 'div .col.search_released.responsive_secondrow ::text')
            loader.add_css('platforms', '.platform_img ::attr(class), .vr_supported ::attr(class)')
            loader.add_css('reviews_summary', '.search_review_summary ::attr(data-tooltip-html)')
            loader.add_css('discount_rate', 'div.search_discount.responsive_secondrow span ::text')
            loader.add_css('original_price', 'div[class="col search_price  responsive_secondrow"] ::text, div[class="col search_price discounted responsive_secondrow"] span strike ::text')
            # loader.add_css('discount_price', 'div.discounted.responsive_secondrow ::text')
            loader.add_xpath('discounted_price', '(.//div[@class="col search_price discounted responsive_secondrow"]/text())[2]')

            yield loader.load_item()
