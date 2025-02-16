import re
from setuptools import setup

with open("src/gh2/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setup(
    name="gh2",
    version=version,
)