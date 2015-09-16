import scrapy
import re
from scrapy.selector import Selector
from dotaVideo.items import DotavideoItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor

class ExampleSpider(CrawlSpider):
        name = "mydota"
        allowed_domains = ["dota.178.com"]
        start_urls = ['http://dota.178.com/video/']
        rules=(
            Rule(LinkExtractor(allow=r"/201509/*"),
            callback="parse_news",follow=True),
        )
        def printcn(suni):
            for i in uni:
                print uni.encode('utf-8')
                
        def parse_news(self,response):
            item = DotavideoItem()
            #item['itemType']=response.url.strip().split('/')[-1][:-5]
            self.get_title(response,item)
            self.get_contentUrl(response,item)
            self.get_img(response,item)
            self.get_time(response,item)
            if item['contentUrl']:
                return item 
            
        def get_title(self,response,item):
            title=response.xpath("//div[@class='title']/h1/text()").extract()
            if title:
                # print 'title:'+title[0][:-5].encode('utf-8')
                item['title']=title

        def get_contentUrl(self,response,item):
            source=response.xpath("//div[@id='text']/p/iframe/@src").extract()
            if source:
                # print 'source'+source[0][:-5].encode('utf-8')
                item['contentUrl']=source
        def get_img(self,response,item):
            imgage=response.xpath("//div[@class='x-video-poster']/img/@src").extract()
            if imgage:
                #print news_url 
                item['img']=imgage
        
        def get_time(self,response,item):
            time=response.xpath("/html/head/meta[@name='Expires']/@content").extract()
            if time:
                # print 'url'+from_url[0].encode('utf-8')       
                item['time']=time    