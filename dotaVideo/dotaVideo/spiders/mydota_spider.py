import scrapy
import re
from scrapy.selector import Selector
from dotaVideo.items import DotavideoItem
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from urlparse import urlparse

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
            #print response.url
            #item['itemType']=response.url.split('/')[-1][:-5]
            parsed_uri = urlparse(response.url)
            domain='{uri.netloc}'.format(uri = parsed_uri)
            item['itemType']=domain
            self.get_title(response,item)
            self.get_contentUrl(response,item)
            self.get_img(response,item)
            self.get_time(response,item)
            self.get_author(response,item)
            if item['contentUrl']:
                return item 
            
        def get_title(self,response,item):
            title=response.xpath("//meta[@name='Title']/@content").extract()
            if title:
                # print 'title:'+title[0][:-5].encode('utf-8')
                item['title']=title[0]
            else: 
                title = response.xpath("//meta[@name='Keywords']/@content").extract()
                if title:
                    item['title']=title[0]

        def get_author(self,response,item):
            author = response.xpath("//meta[@name='Author']/@content").extract()
            if author:
                item['author']=author[0]

        def get_contentUrl(self,response,item):
            source=response.xpath("//div[@id='text']/p/iframe/@src").extract()
            if source:
                # print 'source'+source[0][:-5].encode('utf-8')
                item['contentUrl']=source[0]

        def get_img(self,response,item):
            imgage=response.xpath("//div[@class='x-video-poster']/img/@src").extract()
            if imgage:
                #print news_url 
                item['img']=imgage[0]
        
        def get_time(self,response,item):
            time=response.xpath("//meta[@name='Expires']/@content").extract()
            if time:
                # print 'url'+from_url[0].encode('utf-8')       
                item['time']=time[0] 
            else:
                time = response.xpath("//div[@class='title-info']/span[3]/text()").extract()
                if time:
                    item['time']=time[0][-19:]     


