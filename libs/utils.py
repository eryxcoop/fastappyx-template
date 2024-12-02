import os
import re


def normalize_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"[^\w\s]", "", text)  # Remove punctuation
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra whitespace
    return text


def get_or_raise_error(var):
    try:
        return os.environ[var]
    except KeyError:
        raise KeyError(f"Missing environment variable: {var}")


def get_or_default(var, default):
    try:
        return os.environ[var]
    except KeyError:
        return default


def get_or_default_with_options(var, default, options):
    value = get_or_default(var, default)
    if value not in options:
        raise ValueError(f"Invalid value for {var}: {value}. Must be one of: {', '.join(options)}")
    return value


def is_set_and_true(var, default=False):
    # env vars are always strings, so we need to parse it
    return get_or_default(var, str(default)).lower() in ("yes", "true", "y", "t", "1")


def get_sha256_signature_for(body: dict, secret: str):
    import hmac
    import hashlib
    import json

    return hmac.new(
        secret.encode("utf-8"),
        msg=json.dumps(body).encode("utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()


def first_element_of_list_for(lst, lambda_fn):
    return next(filter(lambda_fn, lst))
