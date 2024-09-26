import os

class Config:
    """Base configuration."""
    # Set the secret key for session management or any other security features
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')

    # Database configuration: change the URI according to your setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///app.db')

    # This setting turns off the Flask-SQLAlchemy modification tracking feature to improve performance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other Flask settings
    DEBUG = False
    TESTING = False


class TestingConfig(Config):
    """Testing configuration."""
    # Use a separate test database (SQLite in-memory in this case)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

    # Enable debug mode
    DEBUG = True

    # Enable testing mode
    TESTING = True

    # Set to False to prevent logging during tests
    SQLALCHEMY_ECHO = False