from setuptools import setup 
import setuptools
  
setup( 
    name='Pyfiles', 
    version='0.1', 
    description='A package to handle all py files.', 
    author='Kalim Mulani', 
    author_email='kalimmulani8@gmail.com', 
    packages=setuptools.find_packages(), 
    install_requires=[ 
        "pandas",
        "numpy",
        "bs4",
        "urlopen",
        "requests",
        "nltk"
    ], 
) 