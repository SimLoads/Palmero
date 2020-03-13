from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='palmero',
    version='0.2.3',
    description='Easy and secure python encryption',
    long_description=long_description,
    url='https://github.com/SimLoads/palmero',
    author='PyGoose',
    author_email='sam@dbndesign.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='encryption decryption security tool',
    py_modules=['palmero'],
    install_requires=['pycryptodome'],
    python_requires='>=3.4'
)