# Temple Web Settings

# one single place to find all the settings/config/constants for the temple web project

from urllib.parse import urljoin
from decouple import config
from importlib import metadata
from decouple import Csv

DEPLOYMENT_VERSION = config(
    "DEPLOYMENT_VERSION", default="TestingLocal-ubuntu23-aahnik"
)


class PaymentGatewayConfig:
    BASE_URL = "https://merchant.upigateway.com/api/"

    CREATE_ORDER = BASE_URL + "create_order"
    CHECK_ORDER_STATUS = BASE_URL + "check_order_status"

    REQUEST_HEADERS = {"Content-Type": "application/json"}

    API_KEY = config("PAYMENT_GATEWAY_API_KEY")

    USER_DEFINED_FIELDS = {"udf1": DEPLOYMENT_VERSION}

    CALLBACK_SLUG = "payment-status"


class MyDjangoSettings:
    DEBUG = config("DEBUG", default=False, cast=bool)
    PROD = config("PROD", default=False, cast=bool)
    PROD_FILES_ROOT = config("PROD_FILES_ROOT", default="/app/data/", cast=str)
    PROD_DOMAIN = config("PROD_DOMAIN", cast=str)
    SECRET_KEY = config("SECRET_KEY", cast=str)
    MORE_ALLOWED_HOSTS = config("MORE_ALLOWED_HOSTS", cast=Csv(), default="127.0.0.1")
    CELERY_BROKER_URL = config(
        "CELERY_BROKER_URL", default="redis://localhost:6379", cast=str
    )
    CELERY_RESULT_BACKEND = config(
        "CELERY_RESULT_BACKEND", default="redis://localhost:6379", cast=str
    )
    DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", cast=str)
    EMAIL_HOST_USER = config("EMAIL_HOST_USER", cast=str)
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", cast=str)


# print(metadata())
# TODO: get project version from pyproject.toml
