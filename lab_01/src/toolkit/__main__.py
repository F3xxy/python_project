import argparse
import sys

from .calculator import calculate
from .converter import convert
from .errors import ToolkitError

HELP_TEXT = """toolkit: консольный набор утилит (калькулятор и конвертер величин)
Команды:
  python -m toolkit calc "EXPRESSION"
      вычислить выражение (числа, + - * / // %, скобки)
  python -m toolkit convert VALUE --from UNIT --to UNIT
      перевести величину
      длина: mm, cm, m, km; масса: g, kg, cn, tn; температура: c, f, k
  python -m toolkit --help
      показать эту справку
"""
def build_parcer(): #конструктор командной строки
    parser = argparse.ArgumentParser(
    prog="toolkit",
    description="Консольный набор утилит: калькулятор и конвертер величин",)
    subparsers = parser.add_subparsers(dest="command", required=True)
    calc_parser = subparsers.add_parser("calc", help="вычислить выражение")
    calc_parser.add_argument("expression", help='выражение, например "2 * (2 + 6)"')

    conv_parser = subparsers.add_parser("convert", help="перевести величину")
    conv_parser.add_argument("value", help="число")
    conv_parser.add_argument("--from", dest="from_unit", required=True, help="исходная единица измерения")#значение сохраняется под парметром from_unit
    conv_parser.add_argument("--to", dest="to_unit", required=True, help="конечная единица измерения")#значение сохраняется под парметром to_unit
    return parser

def prepare_args(args):
    if "calc" in args:
        i = args.index("calc")
        rest = args[i + 1:]
        if "--" not in rest and "-h" not in rest and "--help" not in rest:
            args = args[:i + 1] + ["--"] + rest
    return args


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if argv and argv[0] in ("-h", "--help"):
        print(HELP_TEXT)
        return 0    
    args = build_parcer().parse_args(prepare_args(list(argv)))
    try:
        if args.command == "calc":
            result = calculate(args.expression)
        else:
            result = convert(args.value, args.from_unit, args.to_unit)
    except ToolkitError as error:
        print(error, file=sys.stderr) #любая ошибка - дочерняя от ToolkitError, а значит один except ловит все ошибки
        return 2 #без команды - ошибка 2
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
