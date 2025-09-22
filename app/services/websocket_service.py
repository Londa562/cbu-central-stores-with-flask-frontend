import websocket
import json
from threading import Thread
from flask import session, current_app

class WebSocketService:
    def __init__(self):
        self.ws = None
        self.callbacks = {}

    def connect(self, on_message=None):
        if "access_token" not in session:
            return False
        
        token = session["access_token"]
        ws_url = current_app.config["WS_BASE_URL"].replace("http", "ws")
        url = f"{ws_url}/ws/notifications/?token={token}"

        def _on_message(ws, msg):
            data = json.loads(msg)
            if on_message:
                on_message(data)
            if "type" in data and data["type"] in self.callbacks:
                for cb in self.callbacks[data["type"]]:
                    cb(data)

        self.ws = websocket.WebSocketApp(url, on_message=_on_message)
        Thread(target=self.ws.run_forever, daemon=True).start()
        return True

    def add_callback(self, message_type, callback):
        self.callbacks.setdefault(message_type, []).append(callback)

    def disconnect(self):
        if self.ws:
            self.ws.close()