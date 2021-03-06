import os
import re
import sys

from setuptools import setup


DIRNAME = os.path.abspath(os.path.dirname(__file__))
rel = lambda *parts: os.path.abspath(os.path.join(DIRNAME, *parts))

README = open(rel('README.rst')).read()
INIT_PY = open(rel('flask_flatpages', '__init__.py')).read()
VERSION = re.search("__version__ = '([^']+)'", INIT_PY).group(1)


setup(
    name='Flask-FlatPages',
    version=VERSION,
    url='https://github.com/SimonSapin/Flask-FlatPages',
    license='BSD',
    author='Simon Sapin',
    author_email='simon.sapin@exyr.org',
    maintainer='Padraic Calpin',
    maintainer_email='padraic.calpin93@gmail.com',
    description='Provides flat static pages to a Flask application',
    long_description=README,
    packages=[
        'flask_flatpages'
    ],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask>1.0',
        'PyYAML>3.13',
        'Markdown>=2.5',
        'Jinja2>=2.10.1'
    ],
    tests_require=['Pygments>=1.6'],
    extras_require={
        'tests': ['Pygments>=1.6'],
        'docs': ['Sphinx>=1.4']
    },
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
