from .errors import ConvertError 
from .constants import GROUP, ABSOLUTE_ZERO

#проверка на содержание введёной единицы измерения в группе(GROUP)
def group(unit):
    unit = unit.lower()
    for name, units in GROUP.items():
        if unit in units:
            return name
    raise ConvertError(f"Неизвестная единица измерения: {unit!r}")

#перевод из Цельсия
def to_celc(value, unit):
    if unit == "k":
        return value - 273.15
    if unit == "f":
        return (value - 32) * 5 / 9
    return value

#перевод в Цельсий
def from_celc(value, unit):
    if unit == "k":
        return value + 273.15
    if unit == "f":
        return value * 9 / 5 + 32
    return value

#основное тело конвертера
def convert (value, from_unit, to_unit): 
    value = float(value)
    g1 = group(from_unit)
    g2 = group(to_unit)
    if g1 != g2:
        raise ConvertError("Несовместимые единицы измерений!")
    if g1 == 'temperature':
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        if value < ABSOLUTE_ZERO[from_unit] or value < ABSOLUTE_ZERO[to_unit]:
            raise ConvertError("Температура ниже абсолютного нуля!")
        celcius = to_celc(value, from_unit)
        result = from_celc(value, to_unit)
    else:
        coefficient = GROUP[g1] #возможность несовместимости отсекается выше
        result = (value*coefficient[from_unit.lower()])/(coefficient[to_unit.lower()])
    return float(result)
