#html解析器

import re
from bs4 import BeautifulSoup

class HTMLParse(object):
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)

        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        new_urls= set()
        for link in range(1,100):
            new_url = 'http://www.runoob.com/w3cnote/page/'+str(link)
            new_urls.add(new_url)
            print(new_urls)
        return new_urls

    def _get_new_data(self,page_url,soup):
        data = {}
        data['url'] = page_url
        title = soup.find('div',class_='post-intro').find('h2')
        print(title)
        data['title'] = title.get_text()
        summary = soup.find('div',class_='post-intro').find('p')
        data['summary'] = summary.get_text()
        return data