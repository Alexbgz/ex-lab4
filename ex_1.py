#!/usr/bin/env python3
from librip.gen import field
from librip.gen import gen_random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

print([x for x in field(goods, 'price')])
print([x for x in field(goods, 'title', 'price')])
print([x for x in gen_random(1, 10, 7)])
# Реализация задания 1
