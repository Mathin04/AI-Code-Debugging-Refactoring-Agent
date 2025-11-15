import subprocess
import os
import tempfile

def run_python(code: str):
    with tempfile.TemporaryDirectory() as td:
        fpath = os.path.join(td, "script.py")
        with open(fpath, 'w') as f:
            f.write(code)

        proc = subprocess.run(['python', fpath], capture_output=True, text=True)
        return proc.stdout + proc.stderr

def compile_java(code: str, workdir: str):
    return False, "Java not supported in this environment"

def compile_cpp(code: str, workdir: str):
    return False, "C++ not supported in this environment"

def run_compiled(exe):
    return "Run skipped"
