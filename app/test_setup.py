import os
import sys

# Add the app directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

try:
    from services.api_client import APIClient
    from services.auth_service import AuthService
    from utils.decorators import api_required, role_required
    from config import config
    
    print(" All imports successful!")
    print("Core application structure is correct!")
    
except ImportError as e:
    print(f"Import error: {e}")
    print("Please check your file structure and dependencies")