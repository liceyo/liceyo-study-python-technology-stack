from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

    def write_error(self, status_code, **kwargs):
        self.write("Gosh darnit, user! You caused a %d error." % status_code)


handlers = [
    (r"/hello", IndexHandler)
]
