# -*- coding: utf-8 -*-
from distutils.core import setup
from setuptools import find_packages


setup(
    name='crisp-api',
    version='1.1.14',
    author=u'Valerian Saliou',
    author_email='valerian@valeriansaliou.name',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/crisp-im/python-crisp-api',
    license='MIT - http://opensource.org/licenses/mit-license.php',
    description='Crisp API Python.',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
    ],
    install_requires=[
        'requests',
    ],
    zip_safe=False,
)
