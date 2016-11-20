from setuptools import setup

setup(
    name='hug_raven',
    version='1.0.0',
    description='Hug integration for Sentry',
    url='https://github.com/banteg/hug_raven',
    author='banteg',
    packages=['hug_raven'],
    install_requires=['hug', 'raven'],
)
