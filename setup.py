import io
import os
from pathlib import Path
from setuptools import find_packages, setup

# Metadata of package
NAME = 'document_summary_app'
DESCRIPTION = 'A FastAPI-based document summarization application.'
URL = ''
EMAIL = 'ayush050419@gmail.com'
AUTHOR = 'Ayush Kumar Srivastava'
REQUIRES_PYTHON = '>=3.7.0'

# Define the current directory
pwd = os.path.abspath(os.path.dirname(__file__))

# Function to read the requirements file
def list_reqs(fname='requirements.txt'):
    with io.open(os.path.join(pwd, fname), encoding='utf-8') as f:
        return f.read().splitlines()

# Attempt to read the README file for the long description
try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# Load the package's VERSION file as a dictionary
ROOT_DIR = Path(__file__).resolve().parent
about = {}
with open(ROOT_DIR / 'VERSION') as f:
    _version = f.read().strip()
    about['__version__'] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'document_summary_app': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='None',
    classifiers=[
        'License :: OSI Approved :: None',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
