from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "Food_Delivery_Time_Prediction"
VERSION = "0.0.1"
DESCRIPTION = "This is our machine learning project in modular coding"
AUTHOR_NAME = "Shubham Khairmode"
AUTHOR_EMAIL = "shubhambkhairmode@gmail.com"

REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.strip() for requirement_name in requirement_list]

    return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=get_requirements_list()
)
