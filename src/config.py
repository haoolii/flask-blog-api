# /src/config.py

import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    

app_config = {
    'development': Development,
    'production': Production,
}

# $Env:FLASK_ENV="development"
# export FLASK_ENV="development"
# $Env:DATABASE_URL= "sqlite:////tmp/test87.db"
# export DATABASE_URL="sqlite:////tmp/test87.db"
# $Env:JWT_SECRET_KEY = "87"
# export JWT_SECRET_KEY="87"
