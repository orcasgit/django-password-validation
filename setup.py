from os.path import join
from setuptools import setup, find_packages


long_description = (
    open('README.rst').read() + open('CHANGES.rst').read())


def get_version():
    with open(join('password_validation', '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__ ='):
                return line.split('=')[1].strip().strip('"\'')


setup(
    name='django-password-validation',
    version=get_version(),
    description="Backport of Django 1.9 password validation",
    long_description=long_description,
    author='Erik Romijn',
    author_email='',
    maintainer='ORCAS, Inc',
    maintainer_email='orcastech@orcasinc.com',
    url='https://github.com/orcasgit/django-password-validation/',
    packages=find_packages(),
    package_data={
        'password_validation': ['common-passwords.txt.gz'],
    },
    install_requires=['Django>=1.8.2'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    zip_safe=False,
)
