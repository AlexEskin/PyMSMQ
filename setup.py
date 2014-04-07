from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'pymsmq',
    version = '0.1',
    py_modules = ('pymsmq',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['pywin32>=214h'],

    # Metadata for PyPI:
    author = 'Alex Eskin',
    author_email = 'eskinsqt@gmail.com',
    license = 'MIT',
    url = 'https://github.com/AlexEskin/PyMSMQ',
    keywords = 'msmq',
    description = 'The simplest python msmq library for Windows.',
    long_description = open(normpath(join(dirname(abspath(__file__)),
        'README.md'))).read()

)
