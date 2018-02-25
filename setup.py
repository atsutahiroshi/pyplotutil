from setuptools import setup, find_packages
from os import path
import re

here = path.abspath(path.dirname(__file__))


def long_description(readme):
    with open(path.join(here, readme), 'rt', encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def version(*filepaths):
    with open(path.join(here, *filepaths), 'rt') as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                                  f.read(), re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")


setup(
    name='pyplotutil',
    version=version(),
    description='Plotting utility using matplotlib',
    long_description=long_description(),
    url='https://github.com/atsutahiroshi/pyplotutil',
    author='Hiroshi Atsuta',
    author_email='atsuta.hiroshi@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib'
    ],
    test_suite='tests',
)
