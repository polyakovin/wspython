import os
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler
from tornado.websocket import WebSocketHandler

port = 8000;

class IndexHandler(RequestHandler):
  def get(self):
    self.render("index.html")

class MainHandler(RequestHandler):
  def get(self):
    self.write("Hello, world")

class WsHandler(WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print("WebSocket closed")

def make_app():
  return Application([
    ("/", IndexHandler),
    ("/hello", MainHandler),
    ("/wshello", WsHandler),
  ])

if __name__ == "__main__":
  app = make_app()
  app.listen(port)
  print("Server started on http://localhost:" + str(port))
  IOLoop.current().start()
