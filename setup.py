```python
from setuptools import setup, find_packages

setup(
name='energyhub',
version='0.1',
packages=find_packages(),

description='Système de gestion d\'énergie renouvelable',

install_requires=[
'pandas',
'flask'
],

entry_points={
'console_scripts': [
'energyhub=energyhub.cli:main'
]
},

author='VincentPro',
author_email='contact@energyhub.com',
url='https://github.com/GitHubVincentPro/EnergyHub',

classifiers=[
'Development Status :: 3 - Alpha',
'Intended Audience :: Developers',
'Topic :: Software Development :: Libraries',
'License :: OSI Approved :: MIT License'
]
)
```