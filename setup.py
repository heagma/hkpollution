from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='hkpollution',
   version='1.0',
   description='Get current Hong Kong Pollution for any district',
   license="MIT",
   long_description=long_description,
   author='HeAgMa',
   author_email='heagma@live.com',
   url="https://gitlab.com/heagma/hkpollution",
   packages=['hkpollution'],
   install_requires=['requests'], #external packages as dependencies
)
