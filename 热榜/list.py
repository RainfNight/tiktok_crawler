import requests
import time
from pandas import DataFrame
url='https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&main_billboard_count=5&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=960&browser_language=zh-CN&browser_platform=Win32&browser_name=Edge&browser_version=121.0.0.0&browser_online=true&engine_name=Blink&engine_version=121.0.0.0&os_name=Windows&os_version=10&cpu_core_num=16&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=50&webid=7334970830290126375&msToken=DAjRM7_O4f3PCYej13TEejX8fAHU0FnYP80UIZH9APWaAFAy23n9v6xk3rkDd6dMNC9kaPgS9C4TQmJLLp0surbQA2nC6OcbBEMtW8M_siHRzML84kofrGlm4eS2zo9csBY=&X-Bogus=DFSzswVYESzANJ1itqemdCgNJGbp'
headers={
    'Accept':'application/json, text/plain, */*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'Cookie':'ttwid=1%7C29nR7vcerAXQeE77RuIZiz5yG1OnUv-pJp2SIuKAC1M%7C1707805998%7Cb897f13f758847f7cf74699f4dc33ad81e007494d02ec1e7c17870f5ed8c535c; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; dy_swidth=1707; dy_sheight=960; csrf_session_id=f6878154b9dd1a270993ceb886499b87; strategyABtestKey=%221707806000.454%22; passport_csrf_token=354f2de575b0966a4a4c86931f7ecfe0; passport_csrf_token_default=354f2de575b0966a4a4c86931f7ecfe0; bd_ticket_guard_client_web_domain=2; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; pwa2=%220%7C0%7C3%7C0%22; passport_assist_user=CkABua01PwpfOmxt-KT8lTTEc7OoaqmOA6FKBtLPzeGWtjCBWD9IFEfbWqFvLZ44t31jWicLQsnHoy8ytyWQEhy7GkoKPKCbTPboW2yx3CyJPbH7irIqKkVZyEdgTS2Gpd1cjixeEW2tlq5o7_vLuab33YxUHWVod-JHvjycoWbMYhDXoMkNGImv1lQgASIBAw96DdA%3D; n_mh=cHDDanN7Azl198uw5yAcPZAW1rTOZTVnankKP6gztlg; sso_uid_tt=c937923f783846bae93dd724a5cb65e1; sso_uid_tt_ss=c937923f783846bae93dd724a5cb65e1; toutiao_sso_user=81993e33144b497da001fab272910068; toutiao_sso_user_ss=81993e33144b497da001fab272910068; sid_ucp_sso_v1=1.0.0-KDY0Y2E3MmQ2MmY2MTc5OTZlYTU4MGViNTgyZTkxMGRmMTcwNjcyMzgKHgiN6eDJsMxmEI2nrK4GGO8xIAww1afCqQY4BkD0BxoCaGwiIDgxOTkzZTMzMTQ0YjQ5N2RhMDAxZmFiMjcyOTEwMDY4; ssid_ucp_sso_v1=1.0.0-KDY0Y2E3MmQ2MmY2MTc5OTZlYTU4MGViNTgyZTkxMGRmMTcwNjcyMzgKHgiN6eDJsMxmEI2nrK4GGO8xIAww1afCqQY4BkD0BxoCaGwiIDgxOTkzZTMzMTQ0YjQ5N2RhMDAxZmFiMjcyOTEwMDY4; passport_auth_status=9c63d46731e55adca726ac479c4e37d8%2C; passport_auth_status_ss=9c63d46731e55adca726ac479c4e37d8%2C; uid_tt=c8acc3cfd6384a6290991d204dba27b6; uid_tt_ss=c8acc3cfd6384a6290991d204dba27b6; sid_tt=853c0bba21b1e42bf4bb0416acb2ba0f; sessionid=853c0bba21b1e42bf4bb0416acb2ba0f; sessionid_ss=853c0bba21b1e42bf4bb0416acb2ba0f; publish_badge_show_info=%220%2C0%2C0%2C1707807631891%22; LOGIN_STATUS=1; store-region=cn-js; store-region-src=uid; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=51f136b41b54364bf37d27d7e4596501; __security_server_data_status=1; sid_guard=853c0bba21b1e42bf4bb0416acb2ba0f%7C1707807633%7C5183999%7CSat%2C+13-Apr-2024+07%3A00%3A32+GMT; sid_ucp_v1=1.0.0-KDYyOWI4ZTE0MDVmZDliNTA3MzM0NGJiOTBmMDMzMjEyMGUxYjYyYjAKGgiN6eDJsMxmEJGnrK4GGO8xIAw4BkD0B0gEGgJsZiIgODUzYzBiYmEyMWIxZTQyYmY0YmIwNDE2YWNiMmJhMGY; ssid_ucp_v1=1.0.0-KDYyOWI4ZTE0MDVmZDliNTA3MzM0NGJiOTBmMDMzMjEyMGUxYjYyYjAKGgiN6eDJsMxmEJGnrK4GGO8xIAw4BkD0B0gEGgJsZiIgODUzYzBiYmEyMWIxZTQyYmY0YmIwNDE2YWNiMmJhMGY; download_guide=%223%2F20240213%2F1%22; s_v_web_id=verify_lsk1cquh_0ieMTniT_otEZ_4dMm_9mdE_oTgtVLgDw9md; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A960%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A50%7D%22; __ac_nonce=065cb36670059e49f9e7b; __ac_signature=_02B4Z6wo00f01wIZ5gAAAIDD8OValJ-oL-MCOeKAAKVXVNbtbn9ZSApIQDY32pPOL8W6xjPlMpo9wM9244Wli2hNLDrkIZGLn2y11Dg.hvNUWOhY2lU6YSzon1OrnIajml1qFy4d.7AKzE4sc2; xg_device_score=7.90435294117647; odin_tt=e3c82ddd558621a774d922a631472369ec83cd06fa7713fc2f54d5df53cad96c1dfe21a0277b662eb2765d0b35638c33; tt_scid=GuPppTW1aDyTxOKEiCXyQatQQk2p06IlfcfYZmjdr.Tz.8Yhxy2x32lwnFMGz9G0222f; msToken=-GVx2OBOXt10M5ZY6rXc4F38C8ctZZkzIxMDF6Z2aOzL_KusiXKwWee88jfqyu5D2oXrtq6Uh4EahDS0mn5n14JcVy8V2bNNx4p_G8faF5KY4ugjobra7mslXOb5_oJ5l8g=; IsDouyinActive=true; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCTzZlQ1cwa2tGZC96bENURmRyT21jVkEyaTJtSWdKQk1RZkRQZFcxd1NpUi9LWUFoLzJxTi8rK2lVTFhmMFdYVmE1cE45bGtLOHdJeTlzdWFXdTVreWc9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; msToken=qJGAeteFiyyaV2PUnwaOFkoMVn38huK0cpxzf8oobSsT6AYFKXgfXhqhZ7tjiHCAW75lByJS5M-VrSscXawJwddr-aVvhH_mNpW_dQXAtT1IwLxzzaG-vFFdR_xvYzYarks=',
    'Referer':'https://www.douyin.com/discover?enter=guide'
}
response=requests.get(url,headers=headers)
data_json=response.json()
li=data_json['data']["word_list"]
time_list=[]
rank_list=[]
title_list=[]
url_list=[]
hot_value_list=[]
cover_list=[]
rank=0
for item in li[1:]:
    rank+=1
    timeStamp=int(item["event_time"])
    timeArray = time.localtime(timeStamp)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    time_list.append(otherStyleTime)
    title_list.append(item['word'])
    url_list.append('https://www.douyin.com/hot/'+item['sentence_id'])
    rank_list.append(rank)
    hot_value_list.append(item['hot_value'])
    cover_list.append(item['word_cover']['url_list'])

data={
    '排名':rank_list,
    '标题':title_list,
    '日期':time_list,
    '热度值':hot_value_list,
    '视频链接':url_list,
    '封面链接':cover_list
}
df=DataFrame(data)
df.to_excel('new.xlsx',index=False)