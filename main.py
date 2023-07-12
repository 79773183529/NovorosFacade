from datetime import date
from functools import total_ordering


@total_ordering
class Cassette:
    def __init__(self, width: int, height: int, ral: int = 9006):
        self.width = width
        self.height = height
        self.ral = ral
        self._square = (self.width * self.height) / 1000000
        self._in_production: date | None = None
        self._delivered_to_the_object: date | None = None
        self._mounted: date | None = None

    @property
    def in_production(self):
        return self._in_production

    @in_production.setter
    def in_production(self, the_date: date):
        if isinstance(the_date, date):
            self._in_production = the_date
        else:
            raise ValueError(f"Необходимо ввести дату")

    @property
    def delivered_to_the_object(self):
        return self._delivered_to_the_object

    @delivered_to_the_object.setter
    def delivered_to_the_object(self, the_date: date):
        if isinstance(the_date, date):
            self._delivered_to_the_object = the_date
        else:
            raise ValueError(f"Необходимо ввести дату")

    @property
    def mounted(self):
        return self._mounted

    @mounted.setter
    def mounted(self, the_date: date):
        if isinstance(the_date, date):
            self._mounted = the_date
        else:
            raise ValueError(f"Необходимо ввести дату")

    @property
    def square(self):
        return self._square

    @property
    def _fields(self):
        return self.ral, self.square, self.width, self.height

    def __eq__(self, other):
        if isinstance(other, Cassette):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)

    def __lt__(self, other):
        if isinstance(other, Cassette):
            return self._fields < other._fields
        return NotImplemented

    def __repr__(self):
        return f"Кассета {self.width}*{self.height}(h) RAL{self.ral}"

    def __mul__(self, other):
        if isinstance(other, int):
            lst = []
            for _ in range(other):
                cas = Cassette(self.width, self.height, self.ral)
                cas._in_production = self._in_production
                lst.append(cas)
            return *lst,


class Facade:
    def __init__(self, cassettes: dict[int: list[Cassette]]):
        self.cassettes = cassettes

    def __repr__(self):
        return f"Фасад:\n{self.cassettes}\n"

    @staticmethod
    def _reverse_dict_keys(dictionary):
        reversed_keys_list = list(dictionary.keys())[::-1]  # обращаем список ключей
        return {key: dictionary[key] for key in reversed_keys_list}

    def show_facade(self):
        for key, value in Facade._reverse_dict_keys(self.cassettes).items():
            print(f"ряд {key}: ".ljust(8), end=" ")
            for cas in value:
                print(str(cas).ljust(67), end=" ")
            print()
        print(f"Площадь фасада: {self.square()}м2")
        print(f"Высота  фасада: {self.height()}м")
        print(f"Ширина  фасада: {self.width()}м")

    def show_cassettes(self, *args: Cassette):
        for key, value in Facade._reverse_dict_keys(self.cassettes).items():
            print(f"ряд {key}: ", end=" ")
            for cas in value:
                if cas in args:
                    print(str(cas).ljust(50), end=" ")
                else:
                    print(" * ", end="")
            print()

    def square(self, ral=None):
        total = 0
        for lst in self.cassettes.values():
            for cas in lst:
                try:
                    total += cas.square if not ral or cas.ral == ral else 0
                except AttributeError:
                    print("lst = ", lst)
                    print("cas=", cas)
        return round(total, 2)

    def _change_in_production(self, the_date, row, column):
        self.cassettes[row][column - 1].in_production = the_date

    def put_into_production(self, the_date, row, *args):
        columns = []
        for el in args:
            if isinstance(el, int) or "-" not in el:
                columns.append(el)
            else:
                start, end = map(int, el.split("-"))
                columns.extend([x for x in range(start, end + 1)])
        for column in columns:
            Facade._change_in_production(self, the_date, row, column)

    def get_list_in_production(self, the_date=None):
        lst = []
        for row in self.cassettes.values():
            for cas in row:
                if cas.in_production:
                    if not the_date or the_date == cas.in_production:
                        lst.append(cas)
        return lst

    def get_list_cassette_by_ral_or_size(self, width=None, height=None, ral=None):
        lst = []
        for row in self.cassettes.values():
            for cas in row:
                if (not ral or ral == cas.ral) and (not height or height == cas.height) \
                        and (not width or width == cas.width):
                    lst.append(cas)
        return lst

    def height(self):
        return round(sum([lst[0].height for lst in self.cassettes.values()]) / 1000, 2)

    def width(self):
        return round(max([sum([lst[i].width for i in range(len(lst))]) for lst in self.cassettes.values()]) / 1000, 2)


class Ceiling(Facade):
    def __init__(self, cassettes: dict[int: list[Cassette]]):
        super().__init__(Ceiling._correct_ral_to_dict(cassettes))

    def __repr__(self):
        return f"Потолок:\n{self.cassettes}\n"

    @staticmethod
    def _correct_ral_to_dict(input_dict):
        result_dict = {}
        for key, value in input_dict.items():
            result_dict[key] = list(map(Ceiling._correct_ral, value))
        return result_dict

    @staticmethod
    def _correct_ral(cas: Cassette):
        return Cassette(cas.width, cas.height, 9003)



