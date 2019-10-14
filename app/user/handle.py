from tornado.websocket import WebSocketHandler


class Handle(WebSocketHandler):
    def initialize(self):
        self.set_header('Server', 'Chat-server')

    def open(self):
        pass

    def on_close(self):
        print("Closed")

    def on_message(self, msg):
        print(msg)

    def on_ping(self, data):
        pass

    def check_origin(self, origin):
        return True
