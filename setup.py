from setuptools import find_packages,setup
from typing import List
hyp_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if hyp_dot in requirements:
            requirements.remove(hyp_dot)

setup(
    name='mlproject',
    version='1.0.0',
    author='Irfan',
    author_email='irfangpk2005@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)