import textwrap

from tornado.web import RequestHandler


class ReverseHandler(RequestHandler):
    def get(self, input):
        self.write(input[::-1])


class WrapHandler(RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))


handlers = [
    (r"/reverse/(\w+)", ReverseHandler),
    (r"/wrap", WrapHandler),
]
