from datetime import datetime, timezone

from libs.time_lib.gregorian_datetime import GregorianDateTime


class Clock:
    def __init__(self):
        self._delta_minutes = 0
        self._delta_hours = 0
        self._delta_days = 0

    def now(self):
        _now = datetime.now(tz=timezone.utc)
        _datetime = GregorianDateTime.from_datetime(_now)
        return _datetime.add_minutes(self._delta_minutes).add_hours(self._delta_hours).add_days(self._delta_days)

    def time_is_around(self, gregorian_datetime):
        return self.now().is_around(gregorian_datetime)

    def fast_forward(self, days=0, hours=0, minutes=0):
        self._delta_minutes = minutes
        self._delta_hours = hours
        self._delta_days = days
