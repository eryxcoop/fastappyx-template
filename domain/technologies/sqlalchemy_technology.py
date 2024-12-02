from fastapi import FastAPI
from sqlalchemy.orm import registry

from config_variables import DATABASE_URL
from database_mapping.client import SQLAlchemyDatabaseClient
from domain.repositories.master_persistent_repository import MasterPersistentRepository
from domain.technologies.technology import Technology

sqlalchemy_registry = registry()


class XXXTechnology(Technology):
    @classmethod
    def name(cls):
        return 'SQLALCHEMY'

    def setup_technology_for_test(self):
        connection_options = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
        self._database_client = SQLAlchemyDatabaseClient.for_testing(database_url=DATABASE_URL,
                                                                     mapper_registry=sqlalchemy_registry,
                                                                     connection_options=connection_options)
        MasterPersistentRepository. database_mapper().map_using(sqlalchemy_registry)
        self._database_client.create_database_schema_if_not_exists()

    def setup_technology(self):
        self._webserver = FastAPI()

    def tear_down(self):
        pass

    def new_master_repository(self):
        return MasterPersistentRepository(session=self._database_client.new_session())

    def interfaces(self):
        pass

    def webserver(self):
        return self._webserver

    def expose_http_interface(self, http_interface):
        pass


