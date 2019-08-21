# -*- coding: utf-8 -1 *-
import scrapy
import mysql.connector 

class ConfonetCauseList(scrapy.Spider):
    name = "confonetCauselistNCDRC"       
    allowed_domains = ["http://cms.nic.in"]
    start_urls = [
        'http://cms.nic.in/ncdrcusersWeb/causelist.do?method=loadCauseListViewPub',
    ]
    requestFormDataDict = {"method": "GetHtmlCL",
                        "method":
                         "GetHtml",
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
            yield scrapy.FormRequest(url=url, formdata=requestFormDataDict, callback = self.parse, method='POST', headers = requestFormHeaderDcit, encoding='utf-8', priority=0)
            
    def parse(self, response):
        


