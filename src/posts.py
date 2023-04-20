from datetime import datetime
from secrets import token_hex
from threading import Lock

lock = Lock()
posts = []


def get_posts():
    return posts


def add_post(post):
    posts.append(post)

def get_post(id):
    for post in posts:
        if post['id'] == id:
            return post
    return None


def create_post(msg):
    with lock:
        new_post = {
            'id': len(posts) + 1,
            'msg': msg,
            'timestamp': datetime.utcnow().isoformat(),
            'key': token_hex(40)
        }
        posts.append(new_post)
    return new_post


def delete_post(post_id):
    with lock:
        for i, post in enumerate(posts):
            if post['id'] == post_id:
                del posts[i]
                return True
    return False
