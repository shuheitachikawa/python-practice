import scrapy


class FreelanceLevtechSpider(scrapy.Spider):
    name = 'freelance-levtech'
    allowed_domains = ['freelance.levtech.jp']
    start_urls = ['http://freelance.levtech.jp/']

    def parse(self, response):
        pass
