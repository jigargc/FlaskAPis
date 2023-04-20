from flask import Flask, request, jsonify

from posts import create_post, get_post, delete_post

app = Flask(__name__)


@app.route("/post", methods=["POST"])
def create_posts_controller():
    if not request.data or "msg" not in request.get_json():
        return "No msg found", 400
    msg = request.get_json()['msg']

    if type(msg) != str:
        return "msg must be a string", 400

    if len(msg) == 0:
        return "Empty string found", 400
    post = create_post(msg)
    return jsonify(post)


@app.route("/post/<int:post_id>", methods=["GET"])
def get_post_controller(post_id):
    post = get_post(post_id)
    if not post:
        return "Post not found", 404
    return jsonify(post)

@app.route("/post/<int:post_id>", methods=["DELETE"])
def delete_post_controller(post_id):
    post = get_post(post_id)
    if not post:
        return "Post not found", 404
    delete_post(id)
    return "Post deleted", 200
