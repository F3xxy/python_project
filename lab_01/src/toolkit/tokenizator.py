from .errors import CalcError

def tokenize(expression):
    token = []
    i = 0
    while i < len(expression):
        ch = expression[i]
        two = expression[i:i+2]
        if ch == " ":
            i += 1
        elif two == "//":
            token.append(('oper',two))
            i+=2
        elif ch in "+-*/%":
            token.append(('oper',ch))
            i+=1
        elif expression[i] == "." or expression[i] in "0123456789":
            start = i
            while i < len(expression) and (expression[i]=="." or expression[i] in "0123456789"):
                i+=1
            text = expression[start:i]
            text = float(text)
            token.append(('numb',text))
        elif ch in "()":
            i+=1
            token.append(('paren',ch))
        else:
            pass
            raise CalcError(f"Недопустимый символ: {ch!r}")
            #Кастомные ошибки прописать здесь надо
    return token

#Функция перевода токеннизированного выражения в обратную польскую запись

def RPN(token):
    PRIORITY = {"+": 1, "-": 1, "*": 2, "/": 2, "%": 2, "//": 2, "u-":3, "u+":3}
    output = []
    stack = []
    for kind, value in token:
        if kind == 'numb':
            output.append(value)

        elif kind == 'oper':
            if value in ('u-', 'u+'):
                stack.append(value)
            else:
                while len(stack) > 0 and stack[-1] != "(" and PRIORITY[stack[-1]] >= PRIORITY[value]:
                    output.append(stack.pop())
                stack.append(value)

        elif kind == 'paren' and value == '(':
            stack.append(value)

        elif kind == 'paren' and value == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack:
                stack.pop()
            else:
                raise CalcError("Лишняя закрывающая скобка!")
    while stack:
        top = stack.pop()
        if top == '(':
            raise CalcError ("Незакрытая скобка!")
        output.append(top)
    return output



