from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
setup(
    name="MLOPS-PROJET-1",
    version="0.1",
    author="sordi",
    packages=find_packages(),
    install_requires=requirements,
)