import json
import time

from handle_db import save_fans_info

def response(flow):
    url_list = ['api3-normal-c-lq.amemv.com/aweme/v1/user/follower/list/',
                'api5-normal-c-lq.amemv.com/aweme/v1/user/follower/list/'
                ]
    for url in url_list:

        if url in flow.request.url:
            with open('user.txt','w',encoding='utf-8') as f:
                f.write(flow.response.text)

            for user in json.loads(flow.response.text)['followers']:
                user_info = {}
                user_info['uid'] = user['uid']
                user_info['short_id'] = user['short_id']
                user_info['unique_id'] = user['unique_id']
                user_info['sec_uid'] = user['sec_uid']

                user_info['nickname'] = user['nickname']
                print(user_info['nickname']+'-'*50)
                user_info['gender'] = user['gender']
                user_info['birthday'] = user['birthday']
                #签名
                user_info['signature'] = user['signature']
                user_info['school_name'] = user['school_name']
                user_info['total_favorited'] = user['total_favorited']
                user_info['following_count'] = user['following_count']
                user_info['follower_count'] = user['follower_count']
                user_info['aweme_count'] = user['aweme_count']
                #喜欢的作品数量
                user_info['favoriting_count'] = user['favoriting_count']

                user_info['region'] = user['region']
                user_info['unique_id_modify_time'] = user['unique_id_modify_time']
                user_info['crawl_time'] = int(time.time())


                #暂时不清楚
                user_info['avatar_uri'] = user['avatar_uri']
                #二维码
                user_info['qrcode_url'] = user['share_info']['share_qrcode_url']['url_list'][-1]
                user_info['qrcode_uri'] = user['share_info']['share_qrcode_url']['uri']
                #主页上边的背景图片
                user_info['cover_url'] = user['cover_url'][0]['url_list'][-1]
                user_info['cover_uri'] = user['cover_url'][0]['uri']
                #是否绑定微博
                user_info['is_binded_weibo'] = user['is_binded_weibo']
                user_info['weibo_verify'] = user['weibo_verify']
                user_info['weibo_url'] = user['weibo_url']

                #大头像
                user_info['avatar_medium_url'] = user['avatar_medium']['url_list'][-1]
                user_info['avatar_medium_uri'] = user['avatar_medium']['uri']

                user_info['follow_status'] = user['follow_status']
                #小头像
                user_info['avatar_thumb_url'] = user['avatar_thumb']['url_list'][-1]
                user_info['avatar_thumb_uri'] = user['avatar_thumb']['uri']


                #格式化时间
                # time_local = time.localtime(timestamp)
                # timeArray = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

                # user_info['user_not_show'] = user['user_not_show']
                # user_info['aweme_hotsoon_auth'] = user['aweme_hotsoon_auth']

                save_fans_info(user_info)

"""
mitmdump -s decode_douyin_fans.py -p 8889 
"""