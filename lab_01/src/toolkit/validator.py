from .errors import CalcError

def validate(tokens):
    if not tokens:
        raise CalcError("Введено пустое выражение!")
    pred = None
    for kind, value in tokens:
        if kind == 'numb' and pred is not None:
            if pred[1] == ')' or pred[0] == 'numb':
                raise CalcError("Отсутствие оператора!")
        elif kind == 'paren' and value == '(' and pred is not None:
            if pred[0] == 'numb' or pred[1] == ')':
                raise CalcError("Отсутствие оператора!")
            
        elif kind == 'paren' and value == ')' and pred is not None:
            if pred[0] == 'oper':
                raise CalcError("Отсутствие операнда!")
            if pred[1] == '(':
                raise CalcError("Пустые скобки!")
            
        elif kind == 'paren' and value == ')' and pred is None:
            raise CalcError("Не хватает скобок в начале выражения!")
        
        elif kind == 'oper' and pred is not None:
            if pred[0] == 'oper' and value not in '+-':
                    raise CalcError("Два оператора подряд!")
            if pred[1] == '(' and value not in '+-':
                raise CalcError("Не хватает операнда")
            
        elif kind == 'oper' and value not in '+-'and pred is None:
            raise CalcError("Не хватает операнда в начале выражения!")
        
        pred = (kind, value)
    if pred[0] == 'oper':
        raise CalcError ("Отсутствие операнда!")