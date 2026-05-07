# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2026 Jim Schmitz
#
#   This library is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 2.1 of the License, or (at
#   your option) any later version.
#
#   This library is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
#   General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this library. If not, see <https://www.gnu.org/licenses/>.
#
# *****************************************************************************
import importlib
import sys

# Map the clean CLI subcommand to the actual module name in py5_tools.tools
TOOLS_MAP = {
    "cmd": "py5cmd",
    "translate-imported2module": "py5translate_imported2module",
    "translate-module2imported": "py5translate_module2imported",
    "translate-processingpy2imported": "py5translate_processingpy2imported",
    "utils": "py5utils",
    "run-sketch": "run_sketch",
    "live-coding": "live_coding",
    "install-jdk": "install_jdk",
}


def main():
    args = sys.argv[1:]

    # Check if the user is asking for general help or ran without arguments
    if not args or args[0] in {"-h", "--help"}:
        print("Usage: python -m py5_tools <command> [args...]\n")
        print("Available commands:")
        for cmd in TOOLS_MAP:
            print(f"  {cmd}")
        sys.exit(0)

    # Get the first argument to figure out what the user wants
    command = args[0]
    remaining_args = args[1:]

    if command not in TOOLS_MAP:
        print(f"Error: Unknown command '{command}'\n", file=sys.stderr)
        print("Available commands:", file=sys.stderr)
        for cmd in TOOLS_MAP:
            print(f"  {cmd}", file=sys.stderr)
        sys.exit(1)

    module_name = TOOLS_MAP[command]
    full_module_name = f"py5_tools.tools.{module_name}"

    try:
        # Dynamically load the requested tool module
        module = importlib.import_module(full_module_name)
    except ImportError as e:
        print(f"Error loading {full_module_name}: {e}", file=sys.stderr)
        sys.exit(1)

    # Import the argparse instance from the module
    if not hasattr(module, "parser"):
        print(
            f"Error: {full_module_name} does not expose a 'parser' instance.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Use the instance to parse the remaining command line arguments
    parsed_args = module.parser.parse_args(remaining_args)

    if hasattr(module, "main"):
        module.main(parsed_args)
    else:
        print(
            f"Error: {full_module_name} does not have a 'main' function.",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
