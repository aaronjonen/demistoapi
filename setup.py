from setuptools import setup

setup(
    name='demistoapi',
    version='0.3',
    packages=[
        "demistoapi"
    ],
    license='MIT',
    long_description="Demisto API SDK",
    install_requires=[
       "requests",
        "urllib3"
    ],
    include_package_data=True,
    zip_safe=False
)