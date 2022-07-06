import importlib
import sys
from pkgutil import walk_packages


def import_submodules(package_name):
    """Import all submodules of a module, recursively

    :param package_name: Package name
    :type package_name: str
    :rtype: dict[types.ModuleType]
    """
    package = sys.modules[package_name]

    all = {
        name: importlib.import_module(package_name + "." + name)
        for loader, name, is_pkg in walk_packages(package.__path__)
    }

    return all
