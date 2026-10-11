class ToolkitError(Exception):
    pass

#дочерние ошибки для калькулятора
class CalcError(ToolkitError):
    pass

#дочерние ошибки для конвертера
class ConvertError(ToolkitError):
    pass