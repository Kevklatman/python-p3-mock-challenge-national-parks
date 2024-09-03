class Visitor:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) < 1 or len(value) > 15:
            raise Exception("Invalid name")
        self._name = value

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list(set(trip.national_park for trip in self.trips()))

    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])


class NationalPark:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Invalid name")
        self._name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list(set(trip.visitor for trip in self.trips()))

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitor_counts = {}
        for trip in self.trips():
            visitor = trip.visitor
            visitor_counts[visitor] = visitor_counts.get(visitor, 0) + 1
        return max(visitor_counts, key=visitor_counts.get) if visitor_counts else None

    @classmethod
    def most_visited(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda park: park.total_visits())


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, value):
        if not isinstance(value, Visitor):
            raise Exception("Invalid visitor")
        self._visitor = value

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, value):
        if not isinstance(value, NationalPark):
            raise Exception("Invalid national_park")
        self._national_park = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("Invalid start_date")
        self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        if not isinstance(value, str) or len(value) < 7:
            raise Exception("Invalid end_date")
        self._end_date = value