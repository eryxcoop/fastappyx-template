import datetime


class GregorianDate(datetime.date):
    @classmethod
    def from_date(cls, a_date):
        return cls(year=a_date.year, month=a_date.month, day=a_date.day)

    @classmethod
    def from_string(cls, date_string, date_format="%Y-%m-%d"):
        return cls.from_date(datetime.datetime.strptime(date_string, date_format).date())

    def to_string(self, date_format="%Y-%m-%d"):
        return self.strftime(date_format)
