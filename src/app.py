from flask import Flask, request, jsonify

from posts import create_post, get_post, delete_post, get_posts, get_post_key
from users import get_user, create_user, update_user, get_user_username, get_user_id

app = Flask(__name__)


@app.route("/post", methods=["POST"])
def create_posts_controller():
    try:
        if not request.data or "msg" not in request.get_json():
            raise Exception("msg not found")
        if not request.data or "user_id" not in request.get_json():
            raise Exception("user_id not found")
        msg = request.get_json()['msg']
        user_id = request.get_json()['user_id']
        if type(user_id) != int:
            raise Exception("user_id must be an integer")
        if type(msg) != str:
            raise Exception("msg must be a string")
        if len(msg) == 0:
            raise Exception("Empty string found")
        user = get_user(user_id)
        if not user:
            raise Exception("User not found")
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    post = create_post(msg, user_id)
    return jsonify(post)


@app.route("/post/<int:post_id>", methods=["GET"])
def get_post_controller(post_id):
    post = get_post(post_id)
    if not post:
        return jsonify({"error": "post not found"}), 404
    post['user'] = get_user(post['user_id'])
    return jsonify(post)


@app.route("/post/<string:post_key>", methods=["DELETE"])
def delete_post_controller(post_key):
    post = get_post_key(post_key)
    if not post:
        return jsonify({"error": "post not found"}), 404
    delete_post(post['id'])
    return "Post deleted", 200


@app.route("/user/", methods=["POST"])
def create_user_controller():
    try:
        if not request.data or "username" not in request.get_json():
            raise Exception("username not found")
        if not request.data or "name" not in request.get_json():
            raise Exception("name not found")
        username = request.get_json()['username']
        name = request.get_json()['name']
        if type(username) != str:
            raise Exception("username must be a string")
        if type(name) != str:
            raise Exception("name must be a string")
        if len(username) == 0:
            raise Exception("Empty string found")
        if len(name) == 0:
            raise Exception("Empty string found")
        user = get_user_username(username)
        if user:
            raise Exception("User already exists")
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    user = create_user(username, name)
    return jsonify(user)


@app.route("/user/<int:user_id>", methods=["PUT"])
def update_user_controller(user_id):
    try:
        if not request.data or "name" not in request.get_json():
            raise Exception("name not found")
        name = request.get_json()['name']
        if type(name) != str:
            raise Exception("name must be a string")
        if len(name) == 0:
            raise Exception("Empty string found")
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    user = get_user_id(user_id)
    if not user:
        return jsonify({"error": "user not found"}), 404
    update_user(user['username'], name)
    return "User updated", 200

@app.route("/user/posts/<int:user_id>", methods=["GET"])
def get_user_posts_controller(user_id):
    user = get_user(user_id)
    if not user:
        return "User not found", 404
    posts = []
    for post in get_posts():
        if post['user_id'] == user_id:
            posts.append(post)
    return jsonify(posts)

@app.route("/posts/fullTextSearch/", methods=["GET"])
def get_posts_full_text_search_controller():
    text = request.args.get('text')
    posts = []
    for post in get_posts():
        if not text:
            posts.append(post)
        elif text.lower() in post['msg'].lower():
            posts.append(post)
    for post in posts:
        post['user'] = get_user(post['user_id'])
    return jsonify(posts)


@app.route("/posts/dateRange/", methods=["GET"])
def get_posts_date_range_controller():
    start_datetime_str = request.args.get('start')
    end_datetime_str = request.args.get('end')

    posts = []

    for post in get_posts():
        if not start_datetime_str or not end_datetime_str:
            posts.append(post)
        elif start_datetime_str and not end_datetime_str:
            if start_datetime_str <= post['timestamp']:
                posts.append(post)
        elif not start_datetime_str and end_datetime_str:
            if post['timestamp'] <= end_datetime_str:
                posts.append(post)
        elif start_datetime_str and end_datetime_str:
            if start_datetime_str <= post['timestamp'] <= end_datetime_str:
                posts.append(post)
    for post in posts:
        post['user'] = get_user(post['user_id'])
    return jsonify(posts)


if __name__ == '__main__':
    app.run()
