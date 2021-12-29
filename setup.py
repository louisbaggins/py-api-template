from os import path

from setuptools import find_packages, setup

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='py-api-template',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    version='v1.0.0',
    license='apache-2.0',
    description='Python api template',
    author='Luis Araújo <luisc@take.net>',
    author_email='luisc@take.net',
    url='https://github.com/louisbaggins/py-api-template',
    keywords=[
        'python',
        'blip',
        'chatbot',
        'sdk',
        'api'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ]
)
