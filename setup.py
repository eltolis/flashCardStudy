from setuptools import setup, find_packages
import sys, os

version = '0.8'

setup(name='flashCardStudy',
      version=version,
      description="CLI utility for memorizing and studying.",
      long_description="""\
App designed for studying/memorizing flashcards. You create flashcards in the app and then  you use it to display them in order or randomly.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='GUI flashcard study memorizing',
      author='comatory',
      author_email='',
      url='http://comatory.github.io',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
		  'PrettyTable',
      ],
      entry_points={
		  'console_scripts': ['flashstudy = bin.flashstudy:flashcard']
		  }
      )
