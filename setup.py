from setuptools import find_packages, setup

setuptools.setup(
    name="jfleong_aoc2020",
    version="0.0.1",
    author="J Leong",
    description="my Advent of Code (AOC) 2020 project",
    packages=find_packages("aoc"),
    package_dir={"": "aoc"},
    install_requires=[
        'pytest',
        'pytest-xdist',
    ],
)
