from setuptools import setup
from typing import List


# Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.1"
AUTHOR="Aniruddha Vaze"
DESCRIPTION="This is a first FSDS Nov batch  Machine learning project"
PACKAGES=["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_reqirements_list()->List[str]:
    """
    Description : This function is goining to return list of requirement mention in requirements.txt file

    return this function is going to return a list which contain name of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirements_file:
        return requirements_file.readlines()   



setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION, 
packages=PACKAGES,
install_requires=get_requirements_list()

)


