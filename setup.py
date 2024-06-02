from setuptools import setup, find_packages

setup(
    name="hrconnect",
    version="0.1.0",
    packages=find_packages(where="src"),
    install_requires=[
        "py-bcrypt==0.4",
        "prettytable==3.10.0"
        ]
)