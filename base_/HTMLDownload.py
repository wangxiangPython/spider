#HTML下载器

import requests
import cchardet

class HTMLDownload(object):
    def download(self,url):
        if url is None:
            return
        s= requests.Session()
        s.headers['User-Agent'] = 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 63.0.3239.132Safari / 537.36'
        res = s.get(url)

        if res.status_code==200:
            encoding = cchardet.detect(res.content)['encoding']
            text = res.content.decode(encoding)
            return text

        return None