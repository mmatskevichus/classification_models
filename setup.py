import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="classification_models",
    version="0.0.1",
    author="Forked from https://github.com/qubvel",
    packages= setuptools.find_packages()
)
