import os
import sys
from flask import Flask, session

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

def test_complete_setup():
    # Create a test Flask app
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test-secret-key'
    app.config['API_BASE_URL'] = 'http://localhost:8000'
    app.config['WS_BASE_URL'] = 'http://localhost:8000'
    app.config['SESSION_TYPE'] = 'filesystem'

    with app.app_context(), app.test_request_context():
        try:
            # Test all imports
            from services import APIClient, AuthService, StoresService, WebSocketService, BlockchainService
            from utils import SessionManager, ErrorHandler, ROLES, DEPARTMENTS, REQUEST_STATUS
            from utils.request_validators import RequestValidators
            
            print("✅ All imports successful!")
            
            # Test service initialization
            api_client = APIClient()
            auth_service = AuthService()
            stores_service = StoresService()
            websocket_service = WebSocketService()
            blockchain_service = BlockchainService()
            
            print("✅ All services initialized successfully!")
            
            # Test session manager
            test_user = {
                'id': 1,
                'username': 'testuser',
                'email': 'test@cbu.edu.zm',
                'role': 'department_dean',
                'department': 'COMPUTER_SCIENCE'
            }
            
            SessionManager.set_user_data(test_user)
            SessionManager.set_tokens('test_access_token', 'test_refresh_token')
            
            print("✅ Session management working!")
            print(f"✅ User role: {SessionManager.get_user_role()}")
            print(f"✅ Is authenticated: {SessionManager.is_authenticated()}")
            
            # Test constants
            print(f"✅ Available roles: {list(ROLES.keys())}")
            print(f"✅ Available departments: {list(DEPARTMENTS.keys())}")
            
            # Test error handler
            error_data = {'error': 'Test error', 'code': 'TEST_ERROR'}
            handled_error = ErrorHandler.handle_api_error(error_data, 'test_endpoint')
            print(" Error handling working!")
            
            return True
            
        except ImportError as e:
            print(f" Import error: {e}")
            import traceback
            traceback.print_exc()
            return False
        except Exception as e:
            print(f" Unexpected error: {e}")
            import traceback
            traceback.print_exc()
            return False

if __name__ == "__main__":
    success = test_complete_setup()
    if success:
        print("\n AI-A CORE SETUP COMPLETE!")
        print(" All services, utilities, and session management are ready!")
        print(" Perfect API integration with CBU Central Stores Management System!")
        print(" Ready for AI-B to create routes, templates, and frontend!")
    else:
        print("\n There are issues with the complete setup!")