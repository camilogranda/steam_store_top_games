BOT_NAME = 'steam_store'

SPIDER_MODULES = ['steam_store.spiders']
NEWSPIDER_MODULE = 'steam_store.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
    "timeout": 30 * 1000,  # 30 seconds
}

# Maximun item scraped
CLOSESPIDER_ITEMCOUNT = 100

# Enable cache to fetch responses from local
# HTTPCACHE_ENABLED = False
# HTTPCACHE_EXPIRATION_SECS = 3600

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

