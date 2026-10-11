import argparse
import sys

from .calculator import calculate
from .converter import convert
from .errors import ToolkitError

def build_parcer(): #конструктор командной строки
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="Консольный набор утилит: калькулятор и конвертер величин.",)
    subparsers = parser.add_subparsers(dest="command", required=True)
    calc_parser = subparsers.add_parser("calc", help="вычислить выражение")
    calc_parser.add_argument("expression", help='выражение, например "2 * (2 + 6)"')

    conv_parser = subparsers.add_parser("convert", help="перевести величину")
    conv_parser.add_argument("value", help="число")
    conv_parser.add_argument("--from", dest="from_unit", required=True, help="исходная единица измерениня")
    conv_parser.add_argument("--to", dest="to_unit", required=True, help="конечная единица измерения")
    return parser

def prepare_args(args):
    # Выражение может начинаться с "-" (например "-(2+3)"), argparse принял бы его за опцию.
    # Ставим "--" после "calc", чтобы всё дальше считалось выражением.
    if "calc" in args:
        i = args.index("calc")
        rest = args[i + 1:]
        if "--" not in rest and "-h" not in rest and "--help" not in rest:
            args = args[:i + 1] + ["--"] + rest
    return args


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    args = build_parcer().parse_args(prepare_args(list(argv)))
    try:
        if args.command == "calc":
            result = calculate(args.expression)
        else:
            result = convert(args.value, args.from_unit, args.to_unit)
    except ToolkitError as error:
        print(error, file=sys.stderr)
        return 2
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
