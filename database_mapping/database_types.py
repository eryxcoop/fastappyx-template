from datetime import timezone

from sqlalchemy import DateTime, TypeDecorator, Date

from libs.time_lib.gregorian_date import GregorianDate as DomainDate
from libs.time_lib.gregorian_datetime import GregorianDateTime as DomainDateTime


class GregorianDateTime(TypeDecorator):
    impl = DateTime(timezone=True)

    def process_result_value(self, value, dialect):
        if value is not None:
            if value.tzinfo is None:
                # If the datetime object is naive (no timezone info), assume it's in UTC
                value = value.replace(tzinfo=timezone.utc)
            return DomainDateTime.from_datetime(value)


class GregorianDate(TypeDecorator):
    impl = Date()

    def process_result_value(self, value, dialect):
        if value is not None:
            return DomainDate.from_date(value)
