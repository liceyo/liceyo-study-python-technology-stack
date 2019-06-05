from tornado.web import UIModule
from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        self.render('index.html',books=[1,2,3,4])


class PoemPageHandler(RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb, difference=noun3)

class BookModule(UIModule):
    def render(self, book):
        return self.render_string('module/book.html', book=book*book)

    def embedded_javascript(self):
        return "document.write(\"hi!\")"

    def embedded_css(self):
        return '.book{background-color: green;border-bottom-width: 20px;border-color: chocolate;}'

    def css_files(self):
        return '/static/book.css'

handlers = [
    (r"/index", IndexHandler),
    (r"/poem", PoemPageHandler)
]

ui_modules = {
    'Book':BookModule
}