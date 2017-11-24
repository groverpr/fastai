
# coding: utf-8

"""
Setup script for installing fastai
"""

##########################################################################
## Imports
##########################################################################

from distutils.core import setup


##########################################################################
## Setup
##########################################################################

setup(
    name = "fastai",

    packages = ['fastai'], # this must be the same as the name above

    version = 0.46 ,

    description = "The fast.ai deep learning library, lessons, and tutorials",
    
    author = "Jeremy Howard, Rachel Thomas, Yannet Interian and many others",
    
    author_email = "j@fast.ai",
    
    url = "https://github.com/groverpr/fastai",
    
    download_url =  'https://github.com/groverpr/fastai/archive/0.46.tar.gz',

    install_requires = 
     ['bcolz>=1.1.2',
     'bleach>=2.0.0',
     'certifi>=2016.2.28',
     'cycler>=0.10.0',
     'decorator>=4.1.2',
     'entrypoints>=0.2.3',
     'html5lib>=0.999999999',
     'ipykernel>=4.6.1',
     'ipython>=6.2.0',
     'ipython-genutils>=0.2.0',
     'ipywidgets>=7.0.1',
     'isoweek>=1.3.3',
     'jedi>=0.10.2',
     'Jinja2>=2.9.6',
     'jsonschema>=2.6.0',
     'jupyter>=1.0.0',
     'jupyter-client>=5.1.0',
     'jupyter-console>=5.2.0',
     'jupyter-core>=4.3.0',
     'MarkupSafe>=1.0',
     'matplotlib>=2.0.2',
     'mistune>=0.7.4',
     'nbconvert>=5.3.1',
     'nbformat>=4.4.0',
     'notebook>=5.1.0',
     'numpy>=1.13.1',
     'olefile>=0.44',
     'opencv-python>=3.3.0.10',
     'pandas>=0.20.3',
     'pandas_summary>=0.0.41',
     'pandocfilters>=1.4.2',
     'pexpect>=4.2.1',
     'pickleshare>=0.7.4',
     'Pillow>=4.2.1',
     'prompt-toolkit>=1.0.15',
     'ptyprocess>=0.5.2',
     'Pygments>=2.2.0',
     'pyparsing>=2.2.0',
     'python-dateutil>=2.6.1',
     'pytz>=2017.2',
     'PyYAML>=3.12',
     'pyzmq>=16.0.2',
     'qtconsole>=4.3.1',
     'scipy>=0.19.1',
     'seaborn>=0.8.1',
     'simplegeneric>=0.8.1',
     'six>=1.11.0',
     'terminado>=0.6',
     'testpath>=0.3.1',
     'tornado>=4.5.2',
     'tqdm>=4.15.0',
     'traitlets>=4.3.2',
     'wcwidth>=0.1.7',
     'webencodings>=0.5.1',
     'widgetsnbextension>=3.0.3'],

    keywords = ['deeplearning', 'pytorch', 'machinelearning'],

    classifiers = ['Development Status :: 3 - Alpha'],
)

