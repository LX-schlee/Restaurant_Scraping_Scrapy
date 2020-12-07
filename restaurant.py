import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class RestaurantSpider(CrawlSpider):
    name = 'restaurant'
    allowed_domains = ['tripadvisor.com']
    start_urls = ['https://www.tripadvisor.com/Restaurants-g186605-Dublin_County_Dublin.html']

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@class="wQjYiB7z"]/span/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//a[contains(text(),"Next")]')) 
    )

    def parse_item(self, response):
        yield{
            'title': response.xpath('//div[@class="_1hkogt_o"]/h1/text()').get(),
            'address': response.xpath('//div[@class="xAOpeG9l"]/div/span[2]/a/span/text()').get(),
            'review': response.xpath('(//div[@class="Ct2OcWS4"]/span)/text()[1]').get(),
            'review_count': response.xpath('//a[@class="_3S6pHEQs"]/span/text()[1]').get(),
            'email': response.xpath('(//div[@class="_36TL14Jn _3jdfbxG0"]/span)[2]/a/@href').get().replace('mailto:','').replace('?subject=?',''),
            'phone': response.xpath('//div[@class="_36TL14Jn"]/a/@href').get().strip('tel:') 
        
        
        }
        