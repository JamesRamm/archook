from setuptools import setup, find_packages

setup(
    name='archook',
    version="1.2.0",
    description='Locates arcpy and makes it available to the running python distribution',
    maintainer='James Ramm',
    maintainer_email='jamessramm@gmail.com',
    url='https://github.com/JamesRamm/archook',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Operating System :: Microsoft :: Windows'
    ]
)
