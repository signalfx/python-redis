from setuptools import setup

version = open('VERSION').read()
setup(
    name='redis_opentracing',
    version=version,
    url='https://github.com/opentracing-contrib/python-redis/',
    download_url='https://github.com/opentracing-contrib/python-redis/tarball/'+version,
    license='Apache License 2.0',
    author='Carlos Alberto Cortez',
    author_email='calberto.cortez@gmail.com',
    description='OpenTracing support for Redis',
    long_description=open('README.rst').read(),
    packages=['redis_opentracing'],
    platforms='any',
    install_requires=[
        'future',
        'redis',
        'opentracing>=2.0,<2.4'
    ],
    extras_require={
        'tests': [
            'flake8<3',
            'flake8-quotes',
            'mock<1.1.0',
            'pytest>=2.7,<3',
            'pytest-cov<2.6.0',
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
