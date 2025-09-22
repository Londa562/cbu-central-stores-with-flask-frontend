from functools import wraps
from flask import session, redirect, url_for, flash

def api_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "access_token" not in session:
            flash("Login required", "warning")
            return redirect(url_for("auth.login"))
        return f(*args, **kwargs)
    return wrapper

def role_required(role):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            if "user" not in session or session["user"].get("role") != role:
                flash("Access denied", "danger")
                return redirect(url_for("dashboard.index"))
            return f(*args, **kwargs)
        return wrapper
    return decorator