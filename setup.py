# -*- coding: utf-8 -*-
import setuptools


setuptools.setup(
    name= 'python_tbk',
    version= '0.1',
    description= 'Unmantained Python-TBK with extra arguments to zeep client',
    long_description='Unmantained Python-TBK with extra arguments to zeep client',
    author='MásAVAL DEV Team',
    author_email='dev@masaval.cl',
    url='https://github.com/MasAval/python-tbk',
    packages=['tbk', 'tbk.soap'],
    install_requires=['xmlsec>=1.3.9', 'zeep>=4.0.0'],
    extras_require={
        ':python_version >= "2.7" and python_version < "2.8"': ['typing>=3.6']
    },
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
)
