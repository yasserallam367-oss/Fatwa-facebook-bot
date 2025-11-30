from flask import Flask, request

app = Flask(_name_)

VERIFY_TOKEN = "my_verify_token"

@app.route("/webhook", methods=["GET"])
def verify():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200
    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def receive():
    data = request.json
    print("Received:", data)
    return "OK", 200


if _name_ == "_main_":
    app.run(host="0.0.0.0", port=10000)
