import json
import pprint
import re
import subprocess
import sys
import time

import cchardet
import requests

import urllib3
urllib3.disable_warnings()

def get_response(url,headers):

    res = requests.get(url,headers=headers,verify=False)

    return res

def get_video_data():
    # url = 'https://www.bilibili.com/video/BV1Hz411q7YY'
    # url = 'https://www.bilibili.com/video/BV1Q64y1o77t'
    url = 'https://www.bilibili.com/video/BV14i4y177H1'
    headers = {
        # 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0',
    }
    res = get_response(url,headers)
    encoding = cchardet.detect(res.content)['encoding']
    text = res.content.decode(encoding)
    try:
        title = re.search('<span class="tit">(.*?)</span>',text).group(1)
    except:
        title = re.search('<span class="tit tr-fix">(.*?)</span>',text).group(1)
    print(title)
    video_json = json.loads(re.search('<script>window.__playinfo__=(.*?)</script>',text).group(1))
    print(video_json)

    # pprint.pprint(video_json)
    audio_url = video_json['data']['dash']['audio'][0]['baseUrl']
    # for i in audio_url:
    #     print(i['baseUrl'])
    print(audio_url)
    print('*'*50)
    video_url = video_json['data']['dash']['video'][0]['baseUrl']
    print(video_url)
    # for i in video_url:
    #     print(i['baseUrl'])
    # return (title.strip(),video_url,audio_url)
    return ('test',video_url,audio_url)

def save_video(video_data):
    # video_data = get_video_data()
    headers_video = {
        # 'Host': 'cn-hbwh2-cmcc-bcache-04.bilivideo.com',
        'Connection': 'keep-alive',
        'Access-Control-Request-Method': 'GET',
        'Origin': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36',
        'Access-Control-Request-Headers': 'range',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://www.bilibili.com/video/BV1Hz411q7YY',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }
    headers_audio = {
        # 'Host': 'cn-hbwh2-cmcc-bcache-04.bilivideo.com',
        'Connection': 'keep-alive',
        'Origin': 'https://www.bilibili.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5     Safari/537.36',
        'Accept': '*/*',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Referer': 'https://www.bilibili.com/video/BV1Hz411q7YY',
        'Accept-Encoding': 'identity',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Range': 'bytes=0-4639000'
    }
    audio_content = get_response(video_data[2],headers_audio).content
    video_content = get_response(video_data[1],headers_video).content

    with open(f'{video_data[0]}.mp3','ab+') as f:
        f.write(audio_content)
    # f.flush()

    with open(f'{video_data[0]}.mp4','ab+') as f1:
        f1.write(video_content)
    # f1.flush()

    sys.stdout.flush()


def merge_data(video_name):
    COMMAND = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental output.mp4'
    subprocess.Popen(COMMAND,shell=True)

def main():
    vide_data = get_video_data()
    save_video(vide_data)
    merge_data(vide_data[0])

if __name__ == '__main__':
    main()
    # merge_data('test')