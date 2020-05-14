from setuptools import setup, find_packages

setup(
    name="archook",
    version="1.3.0",
    use_scm_version=True,
    description="Locates arcpy and makes it available to the running python distribution",
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
    setup_requires=['setuptools_scm'],
)
