import sys
from setuptools import setup, find_packages
from pathlib import Path

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (2, 7)
version = '0.2'


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


# This check and everything above must remain compatible with Python 2.7.
if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================
This version of Chargily E-Pay Gateway requires Python {}.{}, but you're trying
to install it on Python {}.{}.
This may be because you are using a version of pip that doesn't
understand the python_requires classifier. Make sure you
have pip >= 9.0 and setuptools >= 24.2, then try again:
    $ python -m pip install --upgrade pip setuptools
    $ python -m pip install chargily_epay_gateway
This will install the latest version of Chargily E-Pay Gateway which works on
your version of Python.
""".format(*(REQUIRED_PYTHON + CURRENT_PYTHON)))
    sys.exit(1)


setup(
    name='chargily_epay_gateway',
    version=version,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    author="Chargily",
    author_email='chargily@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Chargily/epay-gateway-python',
    keywords=['chargily', 'e-payment', 'integration', 'python'],
    install_requires=[
          'requests',
    ],
    project_urls = {
    'Global Website': 'https://chargily.com',
    'DZ Website': 'https://chargily.com.dz',
    'Github': 'https://github.com/Chargily/epay-gateway-python',
    }
)
