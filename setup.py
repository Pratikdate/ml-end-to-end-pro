from setuptools import setup,find_packages

from typing import List  
def get_requires():
    '''this function return a list of packeges required'''
    with open('requirements.txt') as f:
        requirements= f.readlines()
        requirements=[req.replace("\n","") for req in requirements ]
        if "-e ."==requirements:
            requirements.remove('-e .')
    return requirements
    
    


setup(

    name="miproject",
    version='0.0.1',
    author_email="pdate73@gmail.com",
    packages=find_packages(),
    install_require=get_requires(),
)