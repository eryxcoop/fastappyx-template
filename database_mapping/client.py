import contextlib

from sqlalchemy import StaticPool, QueuePool, create_engine
from sqlalchemy.orm import sessionmaker


class SQLAlchemyDatabaseClient:
    @classmethod
    def for_testing(cls, database_url, mapper_registry, connection_options):
        engine = create_engine(database_url, connect_args=connection_options, poolclass=StaticPool)
        return cls(engine, mapper_registry)

    @classmethod
    def for_development(cls, database_url, mapper_registry):
        engine = create_engine(database_url, poolclass=QueuePool)
        return cls(engine, mapper_registry)

    def __init__(self, engine, mapper_registry):
        self._engine = engine
        self._mapper_registry = mapper_registry
        self._session_maker = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        self._session = None

    def create_database_schema_if_not_exists(self):
        self._mapper_registry.metadata.create_all(self._engine)

    def clear_database(self):
        with contextlib.closing(self._engine.connect()) as con:
            trans = con.begin()
            for table in reversed(self._mapper_registry.metadata.sorted_tables):
                con.execute(table.delete())
            trans.commit()
        # self._mapper_registry.metadata.drop_all(self._engine)

    def mapper_registry(self):
        return self._mapper_registry

    def new_session(self):
        return self._session_maker()
