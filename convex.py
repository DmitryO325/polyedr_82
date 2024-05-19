from deq import Deq
from r2point import R2Point


class Figure:  # pragma: no cover
    """ Абстрактная фигура """

    def area(self):
        return 0.0


class Void(Figure):  # pragma: no cover
    """ "Hульугольник" """

    def add(self, p):
        return Point(p)


class Point(Figure):  # pragma: no cover
    """ "Одноугольник" """

    def __init__(self, p):
        self.p = p

    def add(self, q):
        return self if self.p == q else Segment(self.p, q)


class Segment(Figure):  # pragma: no cover
    """ "Двуугольник" """

    def __init__(self, p, q):
        self.p, self.q = p, q

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r)
        elif r.is_inside(self.p, self.q):
            return self
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q)
        else:
            return Segment(self.p, r)


class Polygon(Figure):  # pragma: no cover
    """ Многоугольник """

    def __init__(self, a, b, c):
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._area = abs(R2Point.area(a, b, c))

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self.points.push_first(t)

        return self


if __name__ == "__main__":  # pragma: no cover
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
