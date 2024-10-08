#!/usr/bin/env python3

import argparse

from encoding.growi import cmd as growi_cmd
from encoding.html import cmd as html_cmd


def parse_args():
    parser = argparse.ArgumentParser(
        description="Convert Pukiwiki formatted text data into Growi"
        "importable zipped file."
    )

    subparsers = parser.add_subparsers(required=True)

    growi_subparser = subparsers.add_parser("growi")
    growi_cmd.set_args(growi_subparser)

    html_subparser = subparsers.add_parser("html")
    html_cmd.set_args(html_subparser)

    parser.add_argument(
        "pukiwiki_dump",
        metavar="DUMP_FILE",
        type=argparse.FileType("rb"),
        help="pukiwiki dump file (tar.gz)",
    )

    parser.set_defaults(func=growi_cmd.main)

    parsed_args = parser.parse_args()

    return parsed_args


def main():
    args = parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
