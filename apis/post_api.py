import requests
from config.settings import BASE_URL

class PostAPI:
    def get_post(self,post_id):
        "获取单篇文章"
        url=f"{BASE_URL}/posts/{post_id}"
        return requests.get(url)
    def create_post(self,data):
        "创建一篇文章"
        url=f"{BASE_URL}/posts"
        return requests.post(url,json=data)

