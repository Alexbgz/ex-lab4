# Итератор для удаления дубликатов
class Unique(object):

    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

        self.Ignore_case = kwargs.get('ignore_case')
        self.Items = iter(items)
        self.Passed = set()

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            a = next(self.Items)
            if self.Ignore_case:
                b = str(a)
            else:
                b = str(a).lower()
            if b not in self.Passed:
                self.Passed.add(b)
                return a

    def __iter__(self):
        return self