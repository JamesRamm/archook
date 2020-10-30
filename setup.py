from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()
    
setup(
    name="archook",
    version="1.3.0-dev",
    description="Locates arcpy and makes it available to the running python distribution",
    long_description=long_description,
    long_description_content_type='text/markdown',
    maintainer="Matt Wilkie",
    maintainer_email="matt.wilkie@gov.yk.ca",
    url="https://github.com/JamesRamm/archook",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
    ],
)
