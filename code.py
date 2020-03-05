from home import *

import requests as req
from bs4 import BeautifulSoup as bs
import json

headers = dict()
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36"


q_hash = 'e769aa130647d2354c40ea6a439bfc08'
insta_id = '9201133768'
after = ''
count = 50
x = 1
for i in range(15):

  api_endpoint = f'https://www.instagram.com/graphql/query/?query_hash={q_hash}&variables=%7B%22id%22%3A%22{insta_id}%22%2C%22first%22%3A{count}%2C%22after%22%3A%22{after}%22%7D'

  r = req.get(api_endpoint, headers=headers)
  r_json = r.json()
  end_cursor = r_json['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
  for c in range(count):
      print(x)
      x += 1
      
      try:
        shortcode = r_json['data']['user']['edge_owner_to_timeline_media']['edges'][c]['node']['shortcode']
        print(shortcode)
      except Exception:
        print('process completed')
  after = end_cursor
