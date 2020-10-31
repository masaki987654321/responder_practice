import responder

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    resp.text = "hello world!"

@api.route("/json")
def hello_world_json(req, resp):
    resp.media = {"hello": "world"}

@api.route("/{who}/html")
def hello_world_html(req, resp, *, who):
    resp.html = api.template('hello.html', who=who)

if __name__ == '__main__':
    api.run(port=5000, address='0.0.0.0')