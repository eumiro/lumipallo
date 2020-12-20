"""lumipallo setup
"""

from pathlib import Path

import setuptools

long_description = Path('README.rst').read_text()

setuptools.setup(
    name="lumipallo",
    version="0.0.1",
    author="Miroslav Šedivý",
    author_email='eumiro@gmail.com',
    description="Snowball effect in language learning.",
    extras_require={
        "test": ["pytest"]
    },
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=[],
    url="https://github.com/eumiro/lumipallo",
    packages=setuptools.find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Development Status :: 3 - Alpha",
    ],
)
