from setuptools import setup
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor" 
VERSION="0.0.1"
AUTHOR="Panakj Raj"
DESRCIPTION="This is a first FSDS Nov batch Machine Learing Project"
PACKAGES=["housing"]
REQUIREMENTS_FILE_NAME="requirements.txt"


def get_requirements_list()->[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    
    return This function is going to return a list which contain name
    of libraries mentionered is requirements.txt file
    """

    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESRCIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()



)