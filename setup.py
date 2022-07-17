from setuptools import setup, find_packages
from typing import List

#declaring variables for setup functions
project_name = "Housing-predictor"
version = "0.0.1"
author = "Lingeshwaran S"
description = "First ML Project"
requirement_file_name = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description : This function is going to return list of requirement
    mention in the requirements.txt file

    return : The function is going to return the list of libraries name mentioned in the requirements.txt file.
    """
    with open(requirement_file_name) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(name=project_name,
version=version,
author=author,
description=description,
packages=find_packages(),
install_requires = get_requirements_list()
)