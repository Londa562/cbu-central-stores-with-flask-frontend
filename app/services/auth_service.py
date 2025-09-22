from flask import session
from .api_client import APIClient

class AuthService:
    def __init__(self):
        self.client = APIClient()

    def login(self, username, password):
        return self.client.post("/api/auth/login/", json={"username": username, "password": password})

    def register(self, data):
        return self.client.post("/api/auth/register/", json=data)

    def logout(self):
        resp = self.client.post("/api/auth/logout/")
        session.clear()
        return resp

    def current_user(self):
        return self.client.get("/api/auth/me/")