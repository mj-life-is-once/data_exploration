import json
import os
import subprocess

import psutil


def destroyed(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


def run_notebook(notebook_file, output_path=None, **arguments):
    """Pass arguments to a Jupyter notebook, run it and convert to html."""
    # Create the arguments file
    arguments_path = os.path.join(os.getcwd(), "exploration/jupymodule/arguments.json")

    with open(arguments_path, "w") as fid:
        json.dump(arguments, fid)

    proc = subprocess.Popen(
        [
            "jupyter-nbconvert",
            "--execute",
            "--to",
            "html",
            "--output",
            output_path,
            notebook_file,
        ]
    )

    print(f"Started subprocess with pid{proc.pid}")
    # Clean subprocess
    try:
        proc.wait(timeout=100)
    except subprocess.TimeoutExpired:
        destroyed(proc.pid)
