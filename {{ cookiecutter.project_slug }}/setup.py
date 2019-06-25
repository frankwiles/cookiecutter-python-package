from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Grab the version from bumpversion
with open(path.join(here, ".version"), encoding="utf-8") as f:
    version = f.read()

setup(
    name="{{ cookiecutter.project_slug }}",
    version=version,
    description="{{ cookiecutter.short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=["docs", "tests"]),
    python_requires=">=3.7",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    install_requires=[],
)
