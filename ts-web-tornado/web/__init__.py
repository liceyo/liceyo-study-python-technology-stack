import web.chat_room
import web.hello
import web.poem
import web.string_service

handlers = hello.handlers \
           + string_service.handlers \
           + poem.handlers \
           + chat_room.handlers
ui_modules = poem.ui_modules
