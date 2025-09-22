import requests
from flask import session, current_app
import json

class APIClient:
    def __init__(self):
        self.base_url = current_app.config['API_BASE_URL']
        self.timeout = 30

    def _get_headers(self, headers=None):
        default_headers = {"Content-Type": "application/json"}
        if 'access_token' in session:
            default_headers["Authorization"] = f"Bearer {session['access_token']}"
        if headers:
            default_headers.update(headers)
        return default_headers

    def _handle_response(self, response):
        """Handle API response consistently"""
        try:
            if response.status_code == 401:
                session.clear()
                return {"status": "error", "error": "Authentication required", "code": "UNAUTHORIZED"}
            
            if response.status_code == 403:
                return {"status": "error", "error": "Permission denied", "code": "FORBIDDEN"}
            
            if response.status_code == 404:
                return {"status": "error", "error": "Resource not found", "code": "NOT_FOUND"}
            
            response.raise_for_status()
            
            # Handle empty responses
            if not response.content:
                return {"status": "success", "data": None}
                
            return response.json()
            
        except requests.exceptions.HTTPError as e:
            current_app.logger.error(f"HTTP error: {e}")
            try:
                error_data = response.json()
                return {"status": "error", "error": error_data.get("error", str(e)), "code": "HTTP_ERROR"}
            except:
                return {"status": "error", "error": str(e), "code": "HTTP_ERROR"}
        except json.JSONDecodeError as e:
            current_app.logger.error(f"JSON decode error: {e}")
            return {"status": "error", "error": "Invalid JSON response", "code": "JSON_ERROR"}
        except Exception as e:
            current_app.logger.error(f"Unexpected error: {e}")
            return {"status": "error", "error": "Unexpected error occurred", "code": "UNKNOWN_ERROR"}

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers(kwargs.pop("headers", {}))

        try:
            response = requests.request(
                method, 
                url, 
                headers=headers, 
                timeout=self.timeout, 
                **kwargs
            )
            return self._handle_response(response)
        except requests.exceptions.Timeout:
            current_app.logger.error("Request timeout")
            return {"status": "error", "error": "Request timeout", "code": "TIMEOUT"}
        except requests.exceptions.ConnectionError:
            current_app.logger.error("Connection error")
            return {"status": "error", "error": "Connection error", "code": "CONNECTION_ERROR"}
        except Exception as e:
            current_app.logger.error(f"Request error: {e}")
            return {"status": "error", "error": "Request failed", "code": "REQUEST_ERROR"}

    def get(self, endpoint, **kwargs): 
        return self.request("GET", endpoint, **kwargs)
    
    def post(self, endpoint, **kwargs): 
        return self.request("POST", endpoint, **kwargs)
    
    def put(self, endpoint, **kwargs): 
        return self.request("PUT", endpoint, **kwargs)
    
    def delete(self, endpoint, **kwargs): 
        return self.request("DELETE", endpoint, **kwargs)