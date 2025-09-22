from flask import current_app
from .utils import SessionManager, ROLES, DEPARTMENTS, REQUEST_STATUS, PRIORITY_LEVELS

def inject_global_variables():
    """Inject global variables into all templates"""
    return {
        'current_user': SessionManager.get_user(),
        'is_authenticated': SessionManager.is_authenticated(),
        'user_role': SessionManager.get_user_role(),
        'ROLES': ROLES,
        'DEPARTMENTS': DEPARTMENTS,
        'REQUEST_STATUS': REQUEST_STATUS,
        'PRIORITY_LEVELS': PRIORITY_LEVELS,
        'app_name': 'CBU Central Stores Management System',
        'app_version': '1.0.0'
    }