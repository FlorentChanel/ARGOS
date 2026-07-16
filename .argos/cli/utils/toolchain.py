import os
from logging import getLogger
from shutil import which

logger = getLogger(__name__)


def ensure_compiler_first_in_path() -> None:
    """Prepends the resolved C compiler's directory to PATH (Windows only).

    Environments like git-bash (hooks, IDE git integrations) put Git for
    Windows' own mingw64/usr directories first in PATH. Those ship DLLs with
    the same names as the toolchain's runtime (libgmp-10.dll, zlib1.dll,
    libwinpthread-1.dll, ...), so cc1.exe and the built test binaries load
    incompatible DLLs and die silently. Putting the compiler's directory
    first makes its own DLLs win for every subprocess of the CLI.
    """
    if os.name != "nt":
        return

    compiler = which("cc") or which("gcc")
    if compiler is None:
        return

    compiler_dir = os.path.dirname(compiler)
    entries = os.environ.get("PATH", "").split(os.pathsep)
    if entries and os.path.normcase(entries[0]) == os.path.normcase(compiler_dir):
        return

    logger.debug("Prepending compiler directory to PATH: %s", compiler_dir)
    os.environ["PATH"] = compiler_dir + os.pathsep + os.environ.get("PATH", "")
