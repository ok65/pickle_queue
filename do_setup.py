import sys
text = """
import setuptools
# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as fp:
    long_description = fp.read()
setuptools.setup(name='PickleQueue',
      version='{version}',
      description='Pickleable lightweight Queue Implementation',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Oliver',
      author_email='mail.ok65@googlemail.com',
      url='https://github.com/ok65/pickle_queue',
      packages=['pickle_queue'],
     )
"""
with open("setup.py", "w+") as fp:
    fp.write(text.format(version=sys.argv[1].split('/')[-1]))