# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2021 Jim Schmitz
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
import os
import sys
import shutil
from pathlib import Path
import argparse
import json

from jupyter_client.kernelspec import KernelSpecManager
from IPython.utils.tempdir import TemporaryDirectory


kernel_json = {
    "argv": [
        sys.executable,
        "-m",
        "py5_tools.kernel",
        "-f",
        "{connection_file}"],
    "display_name": "py5",
    "language": "python",
}


def install_py5_kernel_spec(user=True, prefix=None):
    with TemporaryDirectory() as td:
        os.chmod(td, 0o755)  # Starts off as 700, not user readable
        with open(Path(td) / 'kernel.json', 'w') as f:
            json.dump(kernel_json, f, sort_keys=True)

        # Copy any resources
        for file in (Path(__file__).parent / 'resources').glob('*'):
            shutil.copy(file, Path(td) / file.name)

        print('Installing py5 Jupyter kernel spec')
        KernelSpecManager().install_kernel_spec(
            td, 'py5', user=user, prefix=prefix)


def _is_root():
    try:
        return os.geteuid() == 0
    except AttributeError:
        return False  # assume not an admin on non-Unix platforms


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument(
        '--user',
        action='store_true',
        help="Install to the per-user kernels registry. Default if not root.")
    ap.add_argument(
        '--sys-prefix',
        action='store_true',
        help="Install to sys.prefix (e.g. a virtualenv or conda env)")
    ap.add_argument(
        '--prefix', help="Install to the given prefix. "
        "Kernelspec will be installed in {PREFIX}/share/jupyter/kernels/")
    args = ap.parse_args(argv)

    if args.sys_prefix:
        args.prefix = sys.prefix
    if not args.prefix and not _is_root():
        args.user = True

    install_py5_kernel_spec(user=args.user, prefix=args.prefix)


if __name__ == '__main__':
    main()
