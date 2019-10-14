import app
import ssl
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.web import Application


class Endpoint:
    host = "server.autoeid.com"
    port = 9000

    def start(self):
        try:
            certs = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            certs.load_cert_chain("certs/public_key.crt", "certs/private_key.key")
            application = Endpoint.make_app()
            http_server = HTTPServer(application, ssl_options=certs)
            http_server.listen(self.port, self.host)
            app.util.log_info("Server configured")
            IOLoop.instance().start()
            app.util.log_info("Server started")
        except KeyboardInterrupt as e:
            IOLoop.instance().stop()
            app.util.log_info("Server shutting down")
            exit()
        except Exception as e:
            app.util.log_error("Exception in Endpoint -> {}".format(e))

    @staticmethod
    def make_app():
        return Application([
            (r'/endpoint', app.user.Handle)
        ])
