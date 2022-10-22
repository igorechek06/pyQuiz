#!/bin/python
from os import listdir
from os.path import isdir, isfile, join

from PyQt5 import uic


def compile(root: str = "./") -> None:
    init = []

    for name in listdir(root):
        path = join(root, name)

        if name in ["__pycache__"]:
            continue

        if isdir(path):
            compile(path)
            init.append(name)
        elif isfile(path) and path.endswith(".ui"):
            with open(path, "r", encoding="utf-8") as ui:
                with open(f"{path[:-3]}.py", "w") as py:
                    uic.compileUi(ui, py)
                    init.append(name.removesuffix(".ui"))

    with open(join(root, "__init__.py"), "w") as py:
        py.write("\n".join(f"from . import {i}" for i in init))


if __name__ == "__main__":
    compile("./gui")
