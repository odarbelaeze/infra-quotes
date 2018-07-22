"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [
    'falcon',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO: put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='quotes',
    version='0.1.0',
    description='Quotes app in falcon',
    long_description=readme,
    author='Yours truly',
    author_email='odarbelaeze@gmail.com',
    url='...',
    packages=find_packages(include=['quotes', 'quotes.*']),
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='quotes',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: TODO License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
