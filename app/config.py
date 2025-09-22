import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key')
    API_BASE_URL = os.environ.get('API_BASE_URL', 'http://0.0.0.0:8000')
    WS_BASE_URL = os.environ.get('WS_BASE_URL', 'http://0.0.0.0:8000')

    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SESSION_TYPE = "filesystem"
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = False

    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    API_BASE_URL = os.environ.get('PROD_API_URL', 'https://api.cbu-stores.edu.zm')
    WS_BASE_URL = os.environ.get('PROD_WS_URL', 'wss://api.cbu-stores.edu.zm')

class DevelopmentConfig(Config):
    DEBUG = True

config = {
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}