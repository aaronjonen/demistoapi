from setuptools import setup
with open("README.md","r") as fh:
    long_description = fh.read()
setup(
    name='demistoapi',
    version='0.4',
    packages=[
        "demistoapi"
    ],
    license='MIT',
    long_description=long_description,
    install_requires=[
       "requests",
        "urllib3"
    ],
    include_package_data=True,
    zip_safe=False
)