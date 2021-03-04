import os

from setuptools import setup


def read(readmefile):
    return open(os.path.join(os.path.dirname(__file__), readmefile)).read()


setup(
    name="ClementineOPML",
    version="1.0",
    author="Craig Carl",
    author_email="github-projects@gestas",
    description="Simple OPML exporter for the Clementine Player",
    license="MIT",
    keywords="OPML export Celementine",
    url="https://github.com/Gestas/ClementineOPML",
    packages=["ClementineOPML"],
    long_description=read("README.md"),
    python_requires='>=3.8',
    install_requires=['setuptools~=54.0.0', 'lxml~=4.6.2'],
    entry_points={
        "console_scripts": [
            "ClementineOPML=ClementineOPML.ClementineOPML:main",
        ],
    },
)