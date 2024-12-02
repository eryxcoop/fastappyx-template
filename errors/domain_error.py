class DomainError(Exception):
    @classmethod
    def already_logged_in_as_doctor(cls):
        return cls("Already logged in as doctor")

    @classmethod
    def already_logged_in_as_patient(cls):
        return cls("Already logged in as patient")
