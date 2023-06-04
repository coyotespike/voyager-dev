from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read().split('# Contributions and Issues')[0]

setup(
    name='voyager_dev',
    version='0.0.2',
    author='Timothy Roy',
    author_email='tim@gradientflow.ai',
    description='A package for coding assistance',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/coyotespike/voyager-dev',
    packages=['voyager_dev'],
    entry_points={'console_scripts': ['voyager_dev=voyager_dev.voyager_dev:main']},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
