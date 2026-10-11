
import operator

#перечисляем все поддерживаемые операторы
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "//": operator.floordiv} 

#Группы систем измерения (словари)
LENGTH = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0}
MASS = {"g": 0.001, "kg": 1.0, "cn": 100.0, "tn": 1000.0}
TEMPERATURE = {"c", "k", "f"}

#Группы для проверки совместимости
GROUP = {'length': LENGTH, 'mass': MASS, 'temperature': TEMPERATURE}

# Абсолютный ноль по Цельсию, Фаренгейту, Кельвину
ABSOLUTE_ZERO = {"c": -273.15, "k": 0.0, "f": -459.67}