#爬虫调度器

from base_.DataOutput import DataOutput
from base_.HTMLParser import HTMLParse
from base_.HTMLDownload import HTMLDownload
from base_.URLManage import URLManager

class SpiderMan(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HTMLDownload()
        self.parser = HTMLParse()
        self.output = DataOutput()

    def crawl(self,root_url):
        #添加入口url
        self.manager.add_new_url(root_url)
        #判断url管理器中是够有新的url.同时判断抓取多少个url
        while (self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url = self.manager.get_new_url()
                print(new_url)
                html = self.downloader.download(new_url)
                new_urls,data = self.parser.parser(new_url,html)
                # print(new_urls)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print('failed')
                print(e)
            self.output.output_html()

if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl('http://www.runoob.com/w3cnote/page/1')
