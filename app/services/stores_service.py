from flask import current_app
from .api_client import APIClient

class StoresService:
    def __init__(self):
        self.client = APIClient()

    # Authentication API
    def login(self, username, password):
        return self.client.post("/api/auth/login/", json={"username": username, "password": password})

    def register(self, user_data):
        return self.client.post("/api/auth/register/", json=user_data)

    def get_all_users(self):
        return self.client.get("/api/auth/users/")

    def get_current_user(self):
        return self.client.get("/api/auth/me/")

    def logout(self):
        return self.client.post("/api/auth/logout/")

    # Requests API
    def create_request(self, request_data):
        return self.client.post("/api/requests/", json=request_data)

    def get_all_requests(self, filters=None):
        params = filters or {}
        return self.client.get("/api/requests/", params=params)

    def get_request(self, request_id):
        return self.client.get(f"/api/requests/{request_id}/")

    def get_request_details(self, request_id):
        return self.client.get(f"/api/requests/{request_id}/details/")

    def update_request(self, request_id, update_data):
        return self.client.put(f"/api/requests/{request_id}/", json=update_data)

    def delete_request(self, request_id):
        return self.client.delete(f"/api/requests/{request_id}/")

    # Approval Workflow API
    def approve_request(self, request_id, stage_id, approval_data):
        return self.client.post(
            f"/api/requests/{request_id}/approve/{stage_id}/", 
            json=approval_data
        )

    def get_pending_approvals(self):
        return self.client.get("/api/approvals/pending/")

    def get_approval_history(self, request_id):
        return self.client.get(f"/api/requests/{request_id}/history/")

    # Stocks API
    def create_stock(self, stock_data):
        return self.client.post("/api/stocks/", json=stock_data)

    def get_all_stocks(self, filters=None):
        params = filters or {}
        return self.client.get("/api/stocks/", params=params)

    def get_stock(self, stock_id):
        return self.client.get(f"/api/stocks/{stock_id}/")

    def update_stock(self, stock_id, update_data):
        return self.client.put(f"/api/stocks/{stock_id}/", json=update_data)

    def delete_stock(self, stock_id):
        return self.client.delete(f"/api/stocks/{stock_id}/")

    def get_stock_movements(self, stock_id):
        return self.client.get(f"/api/stocks/{stock_id}/movements/")

    def get_low_stock_alerts(self):
        return self.client.get("/api/stocks/alerts/low-stock/")

    def get_categories(self):
        return self.client.get("/api/stocks/categories/")

    # Deliveries API
    def create_delivery(self, delivery_data):
        return self.client.post("/api/deliveries/", json=delivery_data)

    def get_all_deliveries(self):
        return self.client.get("/api/deliveries/")

    def get_delivery(self, delivery_id):
        return self.client.get(f"/api/deliveries/{delivery_id}/")

    def receive_delivery(self, delivery_id, receive_data):
        return self.client.put(f"/api/deliveries/{delivery_id}/", json=receive_data)

    # Damage Reports API
    def report_damage(self, damage_data):
        return self.client.post("/api/report-damage/", json=damage_data)

    def get_all_damage_reports(self):
        return self.client.get("/api/damage-reports/")

    def resolve_damage_report(self, report_id, resolve_data):
        return self.client.put(f"/api/damage-reports/{report_id}/", json=resolve_data)

    # Relocation API
    def relocate_stock(self, relocation_data):
        return self.client.post("/api/relocate/", json=relocation_data)

    def get_all_relocations(self):
        return self.client.get("/api/relocations/")

    # Notifications API
    def get_notifications(self, filters=None):
        params = filters or {}
        return self.client.get("/api/notifications/", params=params)

    def mark_notification_read(self, notification_id):
        return self.client.post(f"/api/notifications/{notification_id}/read/")

    def mark_all_notifications_read(self):
        return self.client.post("/api/notifications/read-all/")

    def get_notification_preferences(self):
        return self.client.get("/api/notification-preferences/")

    def update_notification_preferences(self, preferences_data):
        return self.client.put("/api/notification-preferences/", json=preferences_data)

    # Blockchain API
    def get_blockchain_status(self):
        return self.client.get("/api/blockchain/status/")

    def process_blockchain_events(self):
        return self.client.post("/api/blockchain/process-events/")