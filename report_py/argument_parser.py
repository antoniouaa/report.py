import sys
import argparse

PROG = "report.py"
USAGE = "%(prog)s [--since]"
DESCRIPTION = "A git reporting utility in Python"


class CLIParser(argparse.ArgumentParser):
    def error(self, *args, **kwargs):
        self.print_help()
        sys.exit(1)


def assemble_parser() -> CLIParser:
    parser = CLIParser(
        prog=PROG,
        usage=USAGE,
        description=DESCRIPTION,
    )
    parser.add_argument(
        "--since", help="length of period to collect commits for", default="1 week ago"
    )
    parser.set_defaults(func=parser.print_help)
    return parser
