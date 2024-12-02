class IdentifiableObject:
    def __init__(self):
        self._id = None

    def id(self):
        return self._id

    def has_id(self, id_to_compare) -> bool:
        return self._id == id_to_compare

    def set_id(self, identifier):
        self._id = identifier
