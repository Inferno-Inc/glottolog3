from setuptools import setup, find_packages


setup(
    name='glottolog3',
    version='0.0',
    description='glottolog3',
    long_description='',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld~=4.0',
        'clldmpg~=3.1',
        'clldutils>=1.9.5',
        'markdown',
        'newick>=0.4',
        'pyglottolog~=1.0',
    ],
    extras_require={
        'test': ['pytest-clld>=0.4', 'pytest-cov', 'coverage>=4.2'],
        'dev': ['flake8', 'wheel', 'twine'],
    },
    entry_points={
        'paste.app_factory': ['main=glottolog3:main'],
        'console_scripts': ['glottolog-app=glottolog3.cli:main'],
    },
)
