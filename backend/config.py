class Config:
    """Set Flask config variables."""

    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    JWT_SECRET_KEY = 'supersecretkey'
    RESTX_ERROR_404_HELP = False
    JWT_ACCESS_TOKEN_EXPIRES = 3600