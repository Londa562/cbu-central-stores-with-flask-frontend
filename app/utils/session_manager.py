from flask import session
from datetime import datetime, timedelta
import json

class SessionManager:
    @staticmethod
    def set_user_data(user_data):
        """Store user data in session"""
        session['user'] = {
            'id': user_data.get('id'),
            'username': user_data.get('username'),
            'email': user_data.get('email'),
            'firstname': user_data.get('firstname'),
            'lastname': user_data.get('lastname'),
            'role': user_data.get('role'),
            'department': user_data.get('department'),
            'blockchain_address': user_data.get('blockchain_address')
        }
        session.permanent = True

    @staticmethod
    def set_tokens(access_token, refresh_token):
        """Store authentication tokens"""
        session['access_token'] = access_token
        session['refresh_token'] = refresh_token
        session['token_expiry'] = (datetime.now() + timedelta(hours=1)).isoformat()

    @staticmethod
    def get_user():
        """Get current user from session"""
        return session.get('user', {})

    @staticmethod
    def get_access_token():
        """Get access token from session"""
        return session.get('access_token')

    @staticmethod
    def is_authenticated():
        """Check if user is authenticated"""
        return 'access_token' in session and 'user' in session

    @staticmethod
    def has_role(required_role):
        """Check if user has required role"""
        user = session.get('user', {})
        return user.get('role') == required_role

    @staticmethod
    def has_any_role(required_roles):
        """Check if user has any of the required roles"""
        user = session.get('user', {})
        return user.get('role') in required_roles

    @staticmethod
    def clear_session():
        """Clear all session data"""
        session.clear()

    @staticmethod
    def get_user_role():
        """Get user role"""
        user = session.get('user', {})
        return user.get('role')

    @staticmethod
    def get_user_id():
        """Get user ID"""
        user = session.get('user', {})
        return user.get('id')

    @staticmethod
    def get_user_department():
        """Get user department"""
        user = session.get('user', {})
        return user.get('department')