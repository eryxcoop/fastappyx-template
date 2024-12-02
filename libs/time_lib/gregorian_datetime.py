from datetime import datetime, timedelta


class GregorianDateTime(datetime):
    @classmethod
    def from_datetime(cls, a_datetime):
        return cls(
            year=a_datetime.year,
            month=a_datetime.month,
            day=a_datetime.day,
            hour=a_datetime.hour,
            minute=a_datetime.minute,
            second=a_datetime.second,
            tzinfo=a_datetime.tzinfo,
            microsecond=a_datetime.microsecond,
        )

    def add_minutes(self, minutes: int):
        a_date = self + timedelta(minutes=minutes)
        return self.__class__.from_datetime(a_date)

    def add_hours(self, hours: int):
        a_date = self + timedelta(hours=hours)
        return self.__class__.from_datetime(a_date)

    def add_days(self, days: int):
        a_date = self + timedelta(days=days)
        return self.__class__.from_datetime(a_date)

    def subtract_minutes(self, minutes: int):
        a_date = self - timedelta(minutes=minutes)
        return self.__class__.from_datetime(a_date)

    def is_around(self, gregorian_datetime):
        five_minutes_ahead = self.add_minutes(5)
        five_minutes_behind = self.subtract_minutes(5)
        return five_minutes_behind <= gregorian_datetime <= five_minutes_ahead

    @classmethod
    def from_string(cls, datetime_as_string):
        a_datetime = cls.fromisoformat(datetime_as_string)
        return cls.from_datetime(a_datetime)
