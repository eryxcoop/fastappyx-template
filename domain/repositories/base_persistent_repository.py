from abc import ABC, abstractmethod

from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from errors.element_not_found import ElementNotFound


class BasePersistentRepository(ABC):
    @classmethod
    @abstractmethod
    def database_mapper(cls): ...

    @abstractmethod
    def _domain_class(self): ...

    def __init__(self, session):
        self._session = session
        self._domain_class = self._domain_class()

    def can_store_object(self, an_object) -> bool:
        return isinstance(an_object, self._domain_class)

    def id_of(self, entity) -> int:
        return entity.id()

    def get_for_id(self, entity_id):
        return self.get_by(_id=entity_id)

    def add(self, new_entity):
        self._session.add(new_entity)
        self._session.commit()
        return new_entity

    def add_all(self, entities):
        self._session.add_all(entities)
        self._session.commit()
        return entities

    def exists(self, entity) -> bool:
        return self.exists_by(_id=entity.id)

    def count(self) -> int:
        return self._session.query(self._domain_class).count()

    def all(self):
        return self._session.scalars(select(self._domain_class)).all()

    def get_all_ids(self):
        return self._session.execute(select(self._domain_class._id)).scalars().all()

    def get_by_ids(self, ids):
        return self._session.query(self._domain_class).filter(self._domain_class._id.in_(ids)).all()

    def update(self, entity):
        self._session.commit()
        return entity

    def delete(self, entity):
        self._session.delete(entity)
        self._session.commit()

    def get_by(self, not_found_error_message="Element not found.", if_not_found_do=None, **kwargs):
        try:
            return self._filter_by(**kwargs).one()
        except (NoResultFound, MultipleResultsFound):
            if if_not_found_do:
                return if_not_found_do()
            raise ElementNotFound(not_found_error_message)

    def exists_by(self, **kwargs):
        return self.find_by(**kwargs) is not None

    def find_by(self, **kwargs):
        return self._filter_by(**kwargs).scalar()

    def refresh(self, entity):
        self._session.refresh(entity)
        return entity

    def _filter_by(self, **kwargs):
        filters = (getattr(self._domain_class, column) == value for column, value in kwargs.items())
        return self._session.query(self._domain_class).filter(*filters)
