from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines=file.readlines()
            ## Process each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="fraud_detection_system",
    version="0.0.1",
    author="Usama Afzal",
    author_email="usamafzal36@gmail.com",
    description="A real-time fraud detection system for financial transactions built with MLOPs principles.",
    packages=find_packages(),
    install_requires=get_requirements()
)