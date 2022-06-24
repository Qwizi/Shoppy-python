import os

from setuptools import setup

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()
setup(
    name='shoppy',
    version="1.0.1",
    author='Adrian \'Qwizi\' Ciołek',
    author_email='ciolek.adrian@protonmail.com',
    url='',
    install_requires=install_requires
)
