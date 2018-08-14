from setuptools import setup

setup(
    name='demistoapi',
    version='0.1',
    packages=[
        "demistoapi"
    ],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=[
       "requests",
        "urllib3"
    ],
    include_package_data=True,
    zip_safe=False
)