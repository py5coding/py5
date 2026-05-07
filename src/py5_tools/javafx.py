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
import platform
import sys

import py5_tools

if (
    not py5_tools.is_jvm_running()
    and "JavaFX" in py5_tools.processing.installed_libraries()
):
    try:
        library_dir = None

        os_arch = platform.machine()
        if sys.platform == "darwin":
            if os_arch in ("arm64", "aarch64"):
                # 64-bit ARM
                library_dir = "macos-aarch64"
            elif os_arch == "x86_64":
                # 64-bit Intel
                library_dir = "macos-x86_64"
            # else:
            #     raise RuntimeError(f"Unsupported architecture for MacOS: {os_arch}")
        elif sys.platform == "linux":
            if os_arch == "x86_64":
                # 64-bit Intel
                library_dir = "linux-amd64"
            elif os_arch.startswith("armv"):
                # 32-bit ARM
                library_dir = "linux-arm"
            elif os_arch == "aarch64":
                # 64-bit ARM
                library_dir = "linux-aarch64"
            # else:
            #     raise RuntimeError(f"Unsupported architecture for Linux: {os_arch}")
        elif sys.platform in ["windows", "win32"]:
            if os_arch in ("AMD64", "x86_64"):
                # 64-bit Intel
                library_dir = "windows-amd64"
        #     else:
        #         raise RuntimeError(f"Unsupported architecture for Windows: {os_arch}")
        # else:
        #     raise RuntimeError(f"Unrecognized platform: sys.platform={sys.platform}")

        if library_dir is not None:
            base_path = py5_tools.processing.library_storage_dir()
            py5_tools.add_options(
                f"-Djava.library.path={base_path}/javafx/library/{library_dir}/"
            )
            py5_tools.add_options(
                f"--module-path={base_path}/javafx/library/{library_dir}/modules/"
            )

            py5_tools.add_options(
                "--add-exports=javafx.graphics/com.sun.javafx.geom=ALL-UNNAMED"
            )
            py5_tools.add_options(
                "--add-exports=javafx.graphics/com.sun.glass.ui=ALL-UNNAMED"
            )

            # add all 7 modules
            py5_tools.add_options(
                "--add-modules=javafx.base,javafx.graphics,javafx.swing,javafx.controls,javafx.media,javafx.web,javafx.fxml"
            )
    except Exception as e:
        print(
            f"JavaFX is not properly installed. Please remove JavaFX and possibly try installing it again. Error: {e}",
            file=sys.stderr,
        )


__all__ = []


def __dir__():
    return __all__
