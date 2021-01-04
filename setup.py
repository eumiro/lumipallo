"""
lumipallo setup.py
"""
import re
from pathlib import Path

from setuptools import find_packages, setup

NAME = "lumipallo"
KEYWORDS = ["language learning", "foreign languages"]
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Environment :: Console",
    "Intended Audience :: Education",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: Afrikaans",
    "Natural Language :: Basque",
    "Natural Language :: Bosnian",
    "Natural Language :: Bulgarian",
    "Natural Language :: Catalan",
    "Natural Language :: Croatian",
    "Natural Language :: Czech",
    "Natural Language :: Danish",
    "Natural Language :: Dutch",
    "Natural Language :: English",
    "Natural Language :: Esperanto",
    "Natural Language :: Finnish",
    "Natural Language :: French",
    "Natural Language :: Galician",
    "Natural Language :: German",
    "Natural Language :: Greek",
    "Natural Language :: Hungarian",
    "Natural Language :: Icelandic",
    "Natural Language :: Irish",
    "Natural Language :: Italian",
    "Natural Language :: Latin",
    "Natural Language :: Latvian",
    "Natural Language :: Lithuanian",
    "Natural Language :: Macedonian",
    "Natural Language :: Norwegian",
    "Natural Language :: Polish",
    "Natural Language :: Portuguese",
    "Natural Language :: Portuguese (Brazilian)",
    "Natural Language :: Romanian",
    "Natural Language :: Russian",
    "Natural Language :: Serbian",
    "Natural Language :: Slovak",
    "Natural Language :: Slovenian",
    "Natural Language :: Spanish",
    "Natural Language :: Swedish",
    "Natural Language :: Turkish",
    "Natural Language :: Ukrainian",
    "Natural Language :: Vietnamese",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Education",
    "Topic :: Education :: Computer Aided Instruction (CAI)",
]
INSTALL_REQUIRES = ["xdg"]

# --+----1----+----2----+----3----+----4----+----5----+----6----+----7----+----


if __name__ == "__main__":
    HERE = Path(__file__).resolve().parent
    META_FILE = (HERE / "src" / NAME / "__init__.py").read_text()
    META = dict(
        re.findall(r"^__(\w+)__ = ['\"]([^'\"]*)['\"]", META_FILE, re.M)
    )
    setup(
        name=NAME,
        description=META["description"],
        license=META["license"],
        url=META["url"],
        version=META["version"],
        author=META["author"],
        author_email=META["email"],
        maintainer=META["author"],
        maintainer_email=META["email"],
        keywords=KEYWORDS,
        long_description=Path("README.rst").read_text(),
        long_description_content_type="text/x-rst",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        zip_safe=False,
        classifiers=CLASSIFIERS,
        install_requires=INSTALL_REQUIRES,
        extras_require={"test": ["pytest"]},
        options={},
        include_package_data=True,
        entry_points={
            "console_scripts": ["lumipallo = lumipallo.lumipallo:learn"]
        },
    )
