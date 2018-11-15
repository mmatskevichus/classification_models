import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="classification_models",
    version="0.0.1",
    author="Forked from https://github.com/qubvel",
    description= "Pretrained classification models for Keras",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url= "https://github.com/qubvel/classification_models",
    packages= setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
