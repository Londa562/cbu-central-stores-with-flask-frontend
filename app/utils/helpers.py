from datetime import datetime

def format_date(date_string, format_str="%Y-%m-%d %H:%M:%S"):
    """Format date string to a more readable format"""
    if not date_string:
        return "N/A"
    
    try:
        if isinstance(date_string, str):
            dt = datetime.fromisoformat(date_string.replace('Z', '+00:00'))
        else:
            dt = date_string
            
        return dt.strftime(format_str)
    except (ValueError, AttributeError):
        return "Invalid date"

def format_currency(amount, currency="ZMW"):
    """Format currency amount"""
    if amount is None:
        return "N/A"
    
    try:
        return f"{float(amount):,.2f} {currency}"
    except (ValueError, TypeError):
        return "Invalid amount"