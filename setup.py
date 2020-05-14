from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md')) as f:
    long_description = f.read()
    
setup(
    name="archook",
    version="1.3",
    use_scm_version=True, # overrides version with Git info, if present
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
    setup_requires=['setuptools_scm'], # make available before attempting install
    install_requires=['setuptools_scm'], # keep available after install
)
