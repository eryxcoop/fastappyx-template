from libs.utils import get_or_default_with_options, get_or_raise_error, get_or_default

DATABASE_TECHNOLOGY = get_or_default_with_options("DATABASE_TECHNOLOGY", default="SQLALCHEMY",
                                                  options=["PERFECT", "SQLALCHEMY"])
DATABASE_URL = get_or_default("DATABASE_URL", "sqlite://")
CONVERTION_KEY_HTTP_INTERFACE = get_or_raise_error("CONVERTION_KEY_HTTP_INTERFACE")
