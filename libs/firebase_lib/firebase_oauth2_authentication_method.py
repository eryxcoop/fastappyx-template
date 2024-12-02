import firebase_admin
from firebase_admin import auth, credentials

from errors.authentication_error import AuthenticationError
from libs.firebase_lib.authentication_method import AuthenticationMethod
from libs.firebase_lib.external_profile import ExternalProfile


class FirebaseOauth2AuthenticationMethod(AuthenticationMethod):
    def __init__(self, path_to_service_account_key: str) -> None:
        self._initialize_firebase_app_if_needed(path_to_service_account_key)

    def account_id_from(self, decoded_token):
        return decoded_token["sub"]

    def external_user_profile(self, token):
        try:
            oauth_token = auth.verify_id_token(token)
            return ExternalProfile.from_firebase(oauth_token)
        except Exception:
            raise AuthenticationError.for_invalid_token()

    def _initialize_firebase_app_if_needed(self, path_to_service_account_key):
        try:
            firebase_admin.get_app()
        except ValueError:
            cred = credentials.Certificate(path_to_service_account_key)
            firebase_admin.initialize_app(cred)
