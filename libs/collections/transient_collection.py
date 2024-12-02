from domain.identifiable_object import IdentifiableObject
from errors.element_not_found import ElementNotFound


class TransientCollection:
    def __init__(self, initial_list=None):
        self._current_id = 1
        self._list = initial_list or []

    def add(self, item):
        self._list.append(item)
        if isinstance(item, IdentifiableObject):
            item.set_id(self._current_id)
            self._current_id += 1
        return item

    def first(self):
        return self._list[0]

    def first_or(self, default):
        return self.first() if self.size() > 0 else default

    def filter_by_condition(self, condition) -> "TransientCollection":
        filtered_list = [item for item in self._list if condition(item)]
        return TransientCollection(filtered_list)

    def find_by_condition(self, condition):
        return self.filter_by_condition(condition).first_or(None)

    def remove_by_condition(self, condition):
        self._list = [item for item in self._list if not condition(item)]

    def get_by_condition(self, condition, if_not_found_do=None, not_found_error_message="Element not found."):
        collection = self.filter_by_condition(condition)
        if collection.size() > 1:
            raise Exception("There is more than one element that satisfies the condition.")
        if collection.size() == 0:
            if if_not_found_do:
                return if_not_found_do()
            else:
                raise ElementNotFound(not_found_error_message)
        return collection.first()

    def last(self):
        return self._list[-1]

    def last_or(self, default):
        return self.last() if self.size() > 0 else default

    def get_last_by_condition(self, condition, default=None):
        collection = self.filter_by_condition(condition)
        return collection.last_or(default)

    def remove(self, item):
        return self.remove_by_condition(lambda x: x == item)

    def exists(self, item):
        return item in self._list

    def exists_by_condition(self, condition):
        return self.filter_by_condition(condition).size() == 1

    def clean(self):
        self._list = []

    def size(self):
        return len(self._list)

    def empty(self):
        return self.size() == 0

    def __iter__(self):
        return iter(self._list)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return TransientCollection(self._list[key])
        return self._list[key]

    def __list__(self):
        return self._list
