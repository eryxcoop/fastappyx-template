import abc

from libs.collections.transient_collection import TransientCollection


class BaseTransientRepository:
    def __init__(self):
        self._collection = TransientCollection()

    def can_store_object(self, an_object) -> bool:
        return isinstance(an_object, self._domain_class())

    def id_of(self, entity) -> int:
        return entity.id()

    def get_for_id(self, entity_id):
        return self.collection().get_by_condition(lambda entity: entity._id == entity_id)

    def add(self, new_entity):
        self.collection().add(new_entity)
        return new_entity

    def exists(self, entity) -> bool:
        return self.collection().exists(entity)

    def count(self) -> int:
        return self.collection().size()

    def all(self):
        return list(self.collection())

    def get_all_ids(self):
        return [entity.id() for entity in self.collection()]

    def get_by_ids(self, ids):
        return list(self.collection().filter_by_condition(lambda entity: entity.id() in ids))

    def exists_by_condition(self, condition):
        return self.collection().exists_by_condition(condition)

    def collection(self):
        return self._collection

    def update(self, entity):
        return entity

    def delete(self, entity):
        return self.collection().remove(entity)

    def refresh(self, entity):
        return entity

    @abc.abstractmethod
    def _domain_class(self): ...
