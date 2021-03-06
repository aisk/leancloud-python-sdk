from setuptools import setup, find_packages
from os import path
import sys


here = path.abspath(path.dirname(__file__))

install_requires = [
    'arrow',
    'iso8601',
    'qiniu<=7.1.4',
    'requests>=2.12.1',
    'werkzeug',
]

if sys.version_info < (3, 5, 0):
    install_requires.append('typing')

if sys.version_info < (2, 7, 9):
    install_requires.append('pyOpenSSL')
    install_requires.append('idna')

setup(
    name='leancloud',
    version='2.1.3',
    description='LeanCloud Python SDK',
    url='https://leancloud.cn/',
    author='asaka',
    author_email='lan@leancloud.rocks',
    license='LGPL',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='Leancloud SDK',
    packages=find_packages(exclude=['docs', 'tests*']),
    test_suite='nose.collector',
    install_requires=install_requires,
    extras_require={
        'dev': ['sphinx', 'sphinx_rtd_theme'],
        'test': ['nose', 'wsgi_intercept', 'flask', 'six>=1.9.0'],
    }
)
