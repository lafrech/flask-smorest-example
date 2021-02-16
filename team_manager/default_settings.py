"""Default application settings"""


class DefaultConfig:
    """Default configuration"""
    API_TITLE = "Team Manager API"
    API_VERSION = 0.1
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = '/'
    OPENAPI_JSON_PATH = "api-spec.json"
    OPENAPI_REDOC_PATH = '/'
    OPENAPI_REDOC_URL = (
        "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
