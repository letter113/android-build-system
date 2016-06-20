import os
from setuptools import setup, find_packages

setup(
    name='android_build_system',
    version='0.1.0',
    author='Xin He',
    author_email='letter113@hotmail.com',
    packages=['android_build_system', os.path.join('android_build_system', 'tasks')],
    scripts=['android_build_system/run.py'],
    license='LICENSE',
    entry_points={
          'console_scripts':
              [
                  'abs = android_build_system.run:main',
                  'prerelease = android_build_system.run:main'
              ]
    }
)