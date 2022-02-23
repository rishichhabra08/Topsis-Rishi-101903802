import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Topsis-Rishi-101903802",
    version="1.0.2",
    description="it is designed to provide a user-friendly graphical interface to solve large MCDM problems using TOPSIS",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rishichhabra08/Topsis-Rishi-101903802",
    author="Rishi Chhabra",
    author_email="chhabrarishi844@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["topsis"],
    include_package_data=True,
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={
        "console_scripts": [
            "topsis=topsis.__main__:main",
        ]
    },
)