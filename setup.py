from setuptools import setup, find_packages

setup(
    name="StatisticsTracker",	     # This is the name of your PyPI-package.
    version="0.1.1",		     # Update the version number for new releases
    description="Statistics capture and saving",
    author="Daniel Grecoe",
    author_email="grecoe@microsoft.com",
    url="https://github.com/microsoft/StatisticsTracker",
    license="MIT",
    packages=find_packages(),
    install_requires=["azure-cli"]
)
