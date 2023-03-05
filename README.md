# steam_store_top_games
Web scraper using scrapy-playwright to fetch top 100 sellers games of Steam. Also a web app using ScrapyRT and Flask was created to show the games.

# How to run it?

1. Turn scraper into real-time API with Scrapyrt:
  * Execute this command on terminal: scrapyrt
  * Put in the browser: http://127.0.0.1:9080/crawl.json?start_requests=true&spider_name=steam
  * Refresh the page to execute the spider again.

2. deploy a minimal website with Flask to show the games:
  * On "web" folfer execute: python app.py
  * Put in the browser: http://127.0.0.1:5000

[![stem-top-100-games.png](https://i.postimg.cc/250NYb5q/stem-top-100-games.png)](https://postimg.cc/1gVjczwP)
