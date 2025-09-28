"""
The setup.py file is an essential part of packaging and distributing Python projects. It is used by ssetuptools
(or disutils in older python versions) to define the configuration of your project, such as its metadata, dependencies, and more
"""

from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies.
    :return: List of dependencies
    """
    requirements_list:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)

    except FileNotFoundError:
        pass

    return requirements_list

setup(
    name='textSummarizer',
    version='0.0.1',
    author= 'Bilal Ben Mahria',
    author_email= "bilal.benmahria.up@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)