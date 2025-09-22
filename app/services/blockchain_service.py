from flask import current_app
from .api_client import APIClient

class BlockchainService:
    def __init__(self):
        self.client = APIClient()

    def get_status(self):
        return self.client.get("/api/blockchain/status/")

    def process_events(self):
        return self.client.post("/api/blockchain/process-events/")