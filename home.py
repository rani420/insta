import requests as req
from bs4 import BeautifulSoup as bs
import json

headers = dict()
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.123 Safari/537.36"


class Insta():
  def __init__(self, shortcode):
    self.shortcode = shortcode
    url = f'https://instagram.com/p/{shortcode}'
    resp = req.get(url, headers=headers)
    soup = bs(resp.content, 'html.parser')
    script_tag_text = soup.body.script.text[21:-1]
    json_data = json.loads(script_tag_text)
    json_indent = json.dumps(json_data, indent=4)
    self.url = url
    self.resp = resp
    self.soup = soup
    self.json = json_data
    self.json_indent = json_indent

  def get_images(self):
    try:
        imgs = self.json['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']
        images = []
        for img in imgs:
            t = img['node']['display_url']
            images.append(t)
        return images
    except Exception as e:
        img = self.json['entry_data']['PostPage'][0]['graphql']['shortcode_media']['display_url']
        return img

  def get_desc(self):
    try:
        desc =self.json['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
        return desc
    except Exception as e:
        return short_code_soup.title.text
  def get_videos(self):
    videos_list = []
    try:
      try:
        v = self.json['entry_data']['PostPage'][0]['graphql']['shortcode_media']['video_url']
        return v
      except Exception:
        posts = len(self.json['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'])
        for post in range(posts):
          video_url = self.json['entry_data']['PostPage'][0]['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][post]['node']['video_url']
          videos_list.append(video_url)
        return videos_list
    except Exception:
      return 'no video presen5'

def list_view(l):
  if type(l)==list:
    for x in range(len(l)):
      print(l[x])
  else:
    print(l)

