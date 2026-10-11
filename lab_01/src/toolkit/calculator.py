from .tokenizator import tokenize, RPN
from .errors import CalcError
from .constants import OPERATORS 
from .validator import validate

#Функция подсчёта обратной польской нотации
def evaluate_rpn(rpn):
    stack = []
    for item in rpn:
        if isinstance(item, float):
            stack.append(item)
        else:
            if item == 'u-': #если унарный "-" то меняем знак в стеке
                a = stack.pop()
                stack.append(-a)
            elif item == 'u+': #если унарный "+" то знак остаётся
                pass
            else:
                b = stack.pop()
                a = stack.pop()
                try:
                    res = OPERATORS[item](a,b)
                except ZeroDivisionError:
                    raise CalcError("Деление на ноль!")
                stack.append(res)
    return stack.pop()

#Разметка унарных знаков "+" и "-"
def mark_unar(tokens):
    result = []
    pred = None
    for kind, value in tokens:
        if kind == 'oper' and value in ('-', '+') and (pred is None or pred[0] == 'oper' or pred[1] == '('):
            result.append((kind, 'u'+value)) #склеивание знака перед операндом
        else:
            result.append((kind, value))
        pred = (kind, value)
    return result


def calculate(expression):
    tokens = tokenize(expression)
    validate(tokens)
    tokens = mark_unar(tokens)
    rpn = RPN(tokens)
    result = evaluate_rpn(rpn)
    if result.is_integer():
        return int(result)
    return result
