import requests


API_KEY = "APIKey"

resp = requests.get(
    'http://api.tianapi.com/guonei/',
    params={'key': API_KEY, 'num': 10},
    timeout=10,
)

if resp.status_code == 200:
    data_model = resp.json()
    if data_model.get('code') == 200:
        for news in data_model.get('newslist', []):
            print(news['title'])
            print(news['url'])
            print('-' * 60)
    else:
        print(f"接口返回错误：{data_model.get('msg', '未知错误')}")
else:
    print(f"请求失败，HTTP 状态码：{resp.status_code}")
        


