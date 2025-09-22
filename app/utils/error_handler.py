from flask import jsonify, request, current_app
import traceback

class ErrorHandler:
    @staticmethod
    def handle_api_error(error_data, endpoint=""):
        """Handle API errors consistently"""
        error_message = error_data.get('error', 'Unknown error occurred')
        error_code = error_data.get('code', 'UNKNOWN_ERROR')
        
        current_app.logger.error(f"API Error ({endpoint}): {error_code} - {error_message}")
        
        return {
            'status': 'error',
            'error': error_message,
            'code': error_code
        }

    @staticmethod
    def handle_exception(e, context=""):
        """Handle unexpected exceptions"""
        current_app.logger.error(f"Unexpected error in {context}: {str(e)}")
        current_app.logger.error(traceback.format_exc())
        
        return {
            'status': 'error',
            'error': 'An unexpected error occurred',
            'code': 'UNEXPECTED_ERROR'
        }

    @staticmethod
    def format_validation_errors(errors):
        """Format validation errors for response"""
        formatted_errors = {}
        for field, messages in errors.items():
            if isinstance(messages, list) and len(messages) > 0:
                formatted_errors[field] = messages[0]
            else:
                formatted_errors[field] = str(messages)
        
        return {
            'status': 'error',
            'error': 'Validation failed',
            'details': formatted_errors,
            'code': 'VALIDATION_ERROR'
        }