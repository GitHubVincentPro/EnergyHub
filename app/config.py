import os

class Config:

SECRET_KEY = os.environ.get('SECRET_KEY')

# Database
DB_URI = os.environ.get('DATABASE_URL')

# API
DEBUG = False
TESTING = False

class DevConfig(Config):
DEBUG = True
TESTING = True

class TestConfig(Config):
DEBUG = True
TESTING = True
DB_URI = 'sqlite:///'

config = {
'development': DevConfig,
'testing': TestConfig,
'production': Config
}

def get_config(app_env):
return config[app_env]
