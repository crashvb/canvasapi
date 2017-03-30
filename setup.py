import re
from setuptools import setup

# get version number
with open('canvas_api/__init__.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

setup(
    name='canvas-api',
    version=version,
    description='API wrapper for the Canvas LMS',
    url='https://github.com/ucfopen/canvas-api',
    author='University of Central Florida - Center for Distributed Learning',
    author_email='techrangers@ucf.edu',
    license='MIT License',
    packages=['canvas_api'],
    include_package_data=True,
    install_requires=['requests'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha'
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License'
        'Operating System :: OS Independent'
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
    ],
)