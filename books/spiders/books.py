# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "confonetCauselist"       
    allowed_domains = ["http://cms.nic.in"]
    start_urls = [
        'http://cms.nic.in/ncdrcusersWeb/causelist.do?method=loadCauseListViewPub',
    ]
    requestFormDataDict = {"method": "GetHtmlCL",
                        "method": "GetHtml",
                        "stid": 0,
                        "did": 0,
                        "stdate": "26/07/2019",
                        "selectedDate": "26/07/2019",
                        "stName": "NCDRC",
                        "distName": "NCDRC"}
    requestFormHeaderDict = {"Accept": "text/html, */*; q=0.01",
                            "Accept-Encoding": "gzip, deflate",
                            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
                            "Connection": "keep-alive",
                            "Content-Type": "application/html; charset=utf-8",
                            "Host": "cms.nic.in",
                            "Referer": "http://cms.nic.in/ncdrcusersWeb/causelist.do?method=loadCauseListViewPub",
                            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36",
                            "X-Requested-With": "XMLHttpRequest"}
    def start_request(self):
        for url in start_urls: 
            yield scrapy.FormRequest(url=url, formdata=requestFormDataDict, method='POST', headers = requestFormHeaderDcit, encoding='utf-8', priority=0)
            
    def parse(self, response):
        for book_url in response.css("article.product_pod > h3 > a ::attr(href)").extract():
            yield scrapy.Request(response.urljoin(book_url), callback=self.parse_book_page)
        next_page = response.css("li.next > a ::attr(href)").extract_first()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_book_page(self, response):
        item = {}
        product = response.css("div.product_main")
        item["title"] = product.css("h1 ::text").extract_first()
        item['category'] = response.xpath(
            "//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()"
        ).extract_first()
        item['description'] = response.xpath(
            "//div[@id='product_description']/following-sibling::p/text()"
        ).extract_first()
        item['price'] = response.css('p.price_color ::text').extract_first()
        yield item
