import os

class Config:

SECRET_KEY = os.environ.get('SECRET_KEY')

# Database
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

# API
API_VERSION = 'v1'
DEBUG = True

class DevelopmentConfig(Config):
pass

class ProductionConfig(Config):
DEBUG = False

config = {
'development': DevelopmentConfig,
'production': ProductionConfig
}

def get_config(env_name):
return config[env_name]