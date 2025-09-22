from flask import request
from .validators import validate_email, validate_password, validate_quantity

class RequestValidators:
    @staticmethod
    def validate_login_request():
        """Validate login request data"""
        data = request.get_json()
        errors = {}
        
        if not data.get('username'):
            errors['username'] = 'Username is required'
        
        if not data.get('password'):
            errors['password'] = 'Password is required'
            
        return data, errors

    @staticmethod
    def validate_request_creation():
        """Validate request creation data"""
        data = request.get_json()
        errors = {}
        
        if not data.get('item'):
            errors['item'] = 'Item name is required'
        
        if not data.get('quantity'):
            errors['quantity'] = 'Quantity is required'
        else:
            valid, message = validate_quantity(data['quantity'])
            if not valid:
                errors['quantity'] = message
        
        if not data.get('priority'):
            errors['priority'] = 'Priority is required'
        
        if not data.get('reason'):
            errors['reason'] = 'Reason is required'
            
        return data, errors

    @staticmethod
    def validate_stock_creation():
        """Validate stock creation data"""
        data = request.get_json()
        errors = {}
        
        if not data.get('item_name'):
            errors['item_name'] = 'Item name is required'
        
        if not data.get('original_quantity'):
            errors['original_quantity'] = 'Original quantity is required'
        else:
            valid, message = validate_quantity(data['original_quantity'])
            if not valid:
                errors['original_quantity'] = message
        
        if not data.get('cost_each'):
            errors['cost_each'] = 'Cost per item is required'
        
        if not data.get('location'):
            errors['location'] = 'Location is required'
            
        return data, errors