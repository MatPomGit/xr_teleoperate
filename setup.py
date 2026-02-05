from setuptools import setup, find_packages
import os

deps = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt") as f:
        deps = f.read().splitlines()

setup(
    name="xr_teleoperate",
    version="1.5.0",
    packages=find_packages(),
    install_requires=deps,
    python_requires=">=3.8",
)
