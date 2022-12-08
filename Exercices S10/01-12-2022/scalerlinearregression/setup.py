from setuptools import find_packages, setup


with open('requirements.txt') as f:
    content = f.readlines()

requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='scaler_lr',
      version='1.0',
      description='Contains functions to convert categorical data into ordinal data and scale numerical data in order to apply a linear regression.',
      packages=find_packages(),
      install_requires=requirements)
