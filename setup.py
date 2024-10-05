from setuptools import setup, find_packages
import os

setup(
    name="serch_pharmaceuticals",
    description="measure serch pharmaceuticals interval time",
    version="0.0.1",
    author="GAI-313",
    author_email="nakartogawa.drone@gmail.com",

    install_requires=[
        "opencv-python",
        "pyyaml",
        "pytk"
    ],
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "sp_main = serch_pharmaceuticals:main",
        ]
    }
)