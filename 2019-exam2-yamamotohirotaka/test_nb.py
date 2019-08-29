import subprocess
import tempfile
from pathlib import Path

def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test():
    for entry in Path('.').iterdir():
        if entry.name.endswith(".ipynb"):
            _exec_notebook(entry.name)
