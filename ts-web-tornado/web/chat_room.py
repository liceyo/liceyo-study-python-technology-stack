import json
import logging
import uuid

import tornado.web
import tornado.websocket


class ChatRoom:
    rooms = {}
    callbacks = []

    # 加入聊天室
    def join(self, room_id, callback):
        if room_id not in self.rooms:
            self.rooms[room_id] = []
        self.rooms[room_id].append(callback)

    # 离开聊天室
    def leave(self, callback):
        for room_id in self.rooms:
            self.rooms[room_id].remove(callback)

    # 发送消息
    def send(self, body):
        data = json.loads(body)
        room = self.rooms[data['room_id']]
        for callback in room:
            callback(body)


class MainHandler(tornado.web.RequestHandler):
    def get(self, r_id):
        u_id = uuid.uuid4()
        self.render("chat_room.html", u_id=u_id, r_id=r_id)


class ChatSocketHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        print("new client opened")
        room_id = self.get_argument('room_id')
        self.application.chat_room.join(room_id, self.call_back)

    def on_close(self):
        self.application.chat_room.leave(self.call_back)

    def on_message(self, message):
        logging.info("got message %r", message)
        self.application.chat_room.send(message)

    def call_back(self, message):
        self.write_message(message)


handlers = [
    (r"/chat_room/(\w+)", MainHandler),
    (r"/chat_room_socket", ChatSocketHandler),
]
