from .ColorText import ColorText
from sys import platform
if platform.startswith("win32"):
    from colorama import init
    init()
