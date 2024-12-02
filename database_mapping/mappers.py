from abc import ABC

from sqlalchemy import Table


class DatabaseMapper(ABC):
    def map_using(self, mapper_registry):
        if self._already_mapped(mapper_registry):
            return

        self._map(mapper_registry)

    def _already_mapped(self, mapper_registry): ...

    def _map(self, mapper_registry): ...


class TableMapper(DatabaseMapper):
    def __init__(self, klass, table_name, columns, relationships=None):
        self.klass = klass
        self.table_name = table_name
        self.columns = columns
        self.relationships = relationships or []

    def _already_mapped(self, mapper_registry):
        mapped_classes = [mapper.class_ for mapper in mapper_registry.mappers]
        return self.klass in mapped_classes

    def _map(self, mapper_registry):
        table = Table(self.table_name, mapper_registry.metadata, *self.columns)
        mapper_registry.map_imperatively(self.klass, table, properties=self.relationships)


class CompositeMapper(DatabaseMapper):
    def __init__(self, mappers):
        self._mappers = mappers

    def _already_mapped(self, mapper_registry):
        return len(mapper_registry.mappers) > 0

    def _map(self, mapper_registry):
        for mapper in self._mappers:
            mapper.map_using(mapper_registry)
