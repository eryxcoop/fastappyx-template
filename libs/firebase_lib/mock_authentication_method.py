from errors.authentication_error import AuthenticationError
from libs.firebase_lib.authentication_method import AuthenticationMethod
from libs.firebase_lib.external_profile import ExternalProfile


class MockAuthenticationMethod(AuthenticationMethod):
    def __init__(self, token_fails=False):
        self._token_fails = token_fails

    @classmethod
    def valid_token(cls):
        return "valid_token"

    @classmethod
    def another_valid_token(cls):
        return "another_valid_token"

    @classmethod
    def external_profile_email(cls):
        return "delfi@brea.com"

    """
    Examples Firebase Response:
    {
        "name": "Matias Dinora",
        "picture": "https://lh3.googleusercontent.com/a/ZGNmyxZ4B6_YKcuvjuse5mw8tFenAY1FNYFbWClqfdDeoQ=s96-c",
        "iss": "https://securetoken.google.com/quo-eryx",
        "aud": "quo-eryx",
        "auth_time": 1690478285,
        "user_id": "VOoQVBed3mVvvh1VueFYYzN85Ts1",
        "sub": "VOoQVBed3mVvvh1VueFYYzN85Ts1",
        "iat": 1690478285,
        "exp": 1690481885,
        "email": "mdinora@eryxsoluciones.com.ar",
        "email_verified": True,
        "firebase": {
            "identities": {"google.com": ["117138340238722276350"], "email": ["mdinora@eryxsoluciones.com.ar"]},
            "sign_in_provider": "google.com",
        },
        "uid": "VOoQVBed3mVvvh1VueFYYzN85Ts1",
    }
    """

    def external_user_profile(self, token: str):
        if token not in [self.valid_token(), self.another_valid_token()]:
            raise AuthenticationError.for_invalid_token()
        return ExternalProfile(
            email=self.external_profile_email(),
            image_url="una_imagen",
            external_id="123123",
            full_name="Delfi Brea",
            platform="Firebase",
        )

    def account_id_from(self, decoded_token):
        return decoded_token
