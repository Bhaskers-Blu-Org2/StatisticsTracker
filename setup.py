from setuptools import setup, find_packages

setup(
    name="StatisticsTracker",	     # This is the name of your PyPI-package.
    version="0.1.0",		     # Update the version number for new releases
    description="Statistics capture and saving",
    author="Daniel Grecoe",
    author_email="grecoe@microsoft.com",
    packages=find_packages(),
    install_requires=["azure-cli-core", "azure-storage-blob"]
)
