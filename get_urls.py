import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NameSpider(CrawlSpider):
    name = "isemantics"
    allowed_domains = ["www.isemantics.ai"]
    start_urls = ["https://www.isemantics.ai/"]

    rules = (Rule(LinkExtractor(deny=[r'#', r'resources']), callback="parse_item", follow=True),
            #  Rule(LinkExtractor(allow=r'#'), callback='parse_item',follow=True)
             )

    def parse_item(self, response):
        item = {}
        # item["domain_id"] = response.xpath('//*[@id="content"]').get()
        # item["name"] = response.xpath('//div[@id="name"]').get()
        # item["description"] = response.xpath('//div[@id="description"]').get()
        # print([fun for fun in dir(response) if not fun.startswith('_')])
        # print(response.url)
        item['url'] = response.url
        return item
