import responder

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello world!"

api.run(port=5000, address='0.0.0.0')