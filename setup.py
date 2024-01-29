from setuptools import setup, find_packages

setup(
    name='subBruter',
    version='1.0.2',
    description='subBruter is a tool designed to efficiently probe for alive subdomins from a provided wordlist.',
    author='Bande Aashish',
    url='https://github.com/aashishsec/subBruter',
    packages=find_packages(),
    install_requires=[
        'requests',
        'httpx',
        'colorama',
    ],
    extras_require={
        'dev': ['argparse', 'concurrent.futures'],
    },
    entry_points={
        'console_scripts': [
            'subBruter=subBruter.subBruter:main',
        ],
    },
)


