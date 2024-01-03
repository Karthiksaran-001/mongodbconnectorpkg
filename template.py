import os
import sys
from datetime import datetime
from pathlib import Path 

package_name = "mongodb_package"

list_of_files = [
    ".github/workflows/ci.yaml",
    "src/__init__.py",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/mongodb_curd.py",
    "tests/unit/__init__.py",
    "tests/unit/unit.py",
    "tests/integration/__init__.py",
    "tests/integration/integ.py",
    "_init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiments/experiment.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    fildir , filename = os.path.split(filepath)
    if fildir != "":
        os.makedirs(fildir , exist_ok = True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0):
        with open(filepath , "w"):
            pass ## create an empty file 
        

