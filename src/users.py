from threading import Lock
from secrets import token_hex

users = []
lock = Lock()


def create_user(username, name):
    with lock:
        new_user = {
            'id': len(users) + 1,
            'username': username,
            'name': name,
            'key': token_hex(40)
        }
        users.append(new_user)
    return new_user


def get_user(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None


def get_user_username(username):
    for user in users:
        if user['username'] == username:
            return user
    return None


def get_user_key(key):
    for user in users:
        if user['key'] == key:
            return user
    return None


def get_user_id(user_id):
    for user in users:
        if user['id'] == user_id:
            return user
    return None


def get_users():
    return users


def delete_user(user_id):
    with lock:
        for i, user in enumerate(users):
            if user['id'] == user_id:
                del users[i]
                return True
    return False


def update_user(username, name):
    with lock:
        for i, user in enumerate(users):
            if user['username'] == username:
                users[i]['name'] = name
                return True
    return False
