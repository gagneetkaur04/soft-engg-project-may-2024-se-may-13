class Config:
    """Set Flask config variables."""

    JWT_SECRET_KEY = 'supersecretkey'
    RESTX_ERROR_404_HELP = False
    JWT_ACCESS_TOKEN_EXPIRES = 3600

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_db.sqlite3'