class ExternalProfile:
    FIREBASE_PLATFORM = "firebase"

    def __init__(self, email: str, image_url: str, external_id: str, full_name: str, platform: str):
        self._email = email
        self._image_url = image_url
        self._external_id = external_id
        self._full_name = full_name
        self._platform = platform

    @classmethod
    def from_firebase(cls, oauth_token):
        email = oauth_token.get("email")
        image_url = oauth_token.get("picture")
        external_id = oauth_token.get("uid")
        full_name = oauth_token.get("name")
        return cls(email, image_url, external_id, full_name, cls.FIREBASE_PLATFORM)

    def email(self):
        return self._email

    def image_url(self):
        return self._image_url

    def external_id(self):
        return self._external_id

    def full_name(self):
        return self._full_name

    def first_name(self):
        return " ".join(self._full_name.split()[:-1])

    def last_name(self):
        return self._full_name.split()[-1]

    def platform(self):
        return self._platform
