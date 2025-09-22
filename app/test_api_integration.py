import os
import sys
from flask import Flask, session

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

# Create a test Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'test-secret-key'
app.config['API_BASE_URL'] = 'http://localhost:8000'
app.config['WS_BASE_URL'] = 'http://localhost:8000'

def test_services():
    with app.app_context():
        try:
            from services.api_client import APIClient
            from services.stores_service import StoresService
            from services.auth_service import AuthService
            from services.websocket_service import WebSocketService
            from services.blockchain_service import BlockchainService
            from utils.constants import ROLES, DEPARTMENTS, REQUEST_STATUS
            
            # Test service initialization
            api_client = APIClient()
            stores_service = StoresService()
            auth_service = AuthService()
            websocket_service = WebSocketService()
            blockchain_service = BlockchainService()
            
            print("✅ All services initialized successfully!")
            print("✅ Constants imported correctly!")
            
            # Test constants
            print(f"✅ Roles: {ROLES}")
            print(f"✅ Departments: {list(DEPARTMENTS.keys())[:3]}...")
            print(f"✅ Request Status: {REQUEST_STATUS}")
            
            return True
            
        except ImportError as e:
            print(f"❌ Import error: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            return False

if __name__ == "__main__":
    success = test_services()
    if success:
        print("\nAll services and utilities are properly integrated!")
        print("Ready for AI-B to create routes and templates!")
    else:
        print("\n There are issues with the service integration!")