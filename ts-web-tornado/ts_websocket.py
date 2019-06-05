from uuid import uuid4

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.websocket


class ShoppingCart(object):
    total_inventory = 10
    callbacks = []
    carts = {}

    def register(self, callback):
        self.callbacks.append(callback)

    def unregister(self, callback):
        self.callbacks.remove(callback)

    def move_item_to_cart(self, session):
        if session in self.carts:
            return
        self.carts[session] = True
        self.notify_callbacks()

    def remove_item_from_cart(self, session):
        if session not in self.carts:
            return
        del (self.carts[session])
        self.notify_callbacks()

    def notify_callbacks(self):
        for callback in self.callbacks:
            callback(self.get_inventory_count())

    def get_inventory_count(self):
        return self.total_inventory - len(self.carts)


class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        session = uuid4()
        count = self.application.shoppingCart.get_inventory_count()
        self.render("websocket.html", session=session, count=count)


class CartHandler(tornado.web.RequestHandler):
    def post(self):
        action = self.get_argument('action')
        session = self.get_argument('session')
        if not session:
            self.set_status(400)
            return
        if action == 'add':
            self.application.shoppingCart.move_item_to_cart(session)
        elif action == 'remove':
            self.application.shoppingCart.remove_item_from_cart(session)
        else:
            self.set_status(400)


class StatusHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        self.application.shoppingCart.register(self.callback)

    def on_close(self):
        self.application.shoppingCart.unregister(self.callback)

    def on_message(self, message):
        print(message)
        pass

    def callback(self, count):
        print(count)
        self.write_message('{"inventoryCount":"%d"}' % count)


class Application(tornado.web.Application):
    def __init__(self):
        self.shoppingCart = ShoppingCart()
        handlers = [
            (r'/', DetailHandler),
            (r'/cart', CartHandler),
            (r'/cart/status', StatusHandler)
        ]
        settings = {
            'template_path': 'templates',
            'static_path': 'static'
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
