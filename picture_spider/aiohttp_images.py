import os
import asyncio  #并发任务
import time

import aiohttp  #完成网络请求并发任务
import requests

if not os.path.exists('./images/'):
    os.mkdir('./images/')

#异步编程
async def get_content(link):
    async with aiohttp.ClientSession() as session:
        response = await session.get(link)
        content = await response.read()
        return content

async def download(img):
    content = await get_content(img[1])
    with open(f'./images/{str(img[0])}.jpg','wb') as f:
        f.write(content)
    print(f'下载成功{str(img[1])}')

def run():
    start = time.time()
    base_url= 'https://www.zcool.com.cn/work/content/show?p=2&objectId=6455837'
    response = requests.get(base_url)
    image_list = response.json()['data']['allImageList']
    #创建协程对象
    loop= asyncio.get_event_loop()
    #指定协程执行的任务
    tasks = [asyncio.ensure_future(download((i,image['url'])))for i,image in enumerate(image_list)]
    #运行
    loop.run_until_complete(asyncio.wait(tasks))
    end = time.time()
    print(f"共运行了{end-start}")

if __name__ == '__main__':
    run()