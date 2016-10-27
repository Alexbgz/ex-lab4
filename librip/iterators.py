# Итератор для удаления дубликатов
class Unique(object):

    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False
        if 'ignore_case' in kwargs.keys():
            self.Ignore_case = kwargs['ignore_case']
        else:
            self.Ignore_case = False
        self.Items = list(items)
        self.Passed = set()

    def __next__(self):
        # Нужно реализовать __next__
        while True:
            if self.Index == len(self.Items) - 1:
                raise StopIteration
            self.Index += 1
            a = str(self.Items[self.Index])
            if self.Ignore_case:
                b = a
            else:
                b = a.lower()
            if b not in self.Passed:
                self.Passed.add(b)
                return a

    def __iter__(self):
        self.Index = -1
        return self