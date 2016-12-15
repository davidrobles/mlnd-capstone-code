from setuptools import setup, find_packages

# with open('README.md') as f:
#     readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(name='sample',
      version='0.0.1',
      description='Capstone Project for Udacity Machine Learning Nanodegree',
      # long_description=readme,
      author='David Robles',
      author_email='drobles@gmail.com',
      url='https://github.com/davidrobles/mlnd-capstone-code',
      license='MIT',
      packages=find_packages(exclude=('tests', 'docs')))
