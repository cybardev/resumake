#!/usr/bin/env python3

import argparse
import os
import sys
from importlib.machinery import SourceFileLoader
from importlib.util import module_from_spec, spec_from_loader

from ..utils import generate_resume


def main(args: argparse.Namespace):
    # set paths to resume file
    full_path = os.path.abspath(args.resume)
    filename = os.path.basename(full_path)
    sys.path.append(os.path.dirname(full_path))

    # import resume file as module
    loader = SourceFileLoader(filename, full_path)
    spec = spec_from_loader(filename, loader)
    resume_info = module_from_spec(spec)
    loader.exec_module(resume_info)

    # use author info from resume module to generate resume
    generate_resume(resume_info.main(), args.output)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="resume",
        description="Generate a resume from a given python file",
        allow_abbrev=False,
    )
    parser.add_argument(
        "resume",
        metavar="RESUME",
        type=str,
        help="path to the Python file containing the resume data",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        type=str,
        help="path to the output directory",
        default="./",
    )
    return parser.parse_args()


if __name__ == "__main__":
    main(args=parse_args())
