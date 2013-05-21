from setuptools import setup, find_packages

setup(
    name="folder",
    version='1.2.1',
    description="Folder creation for testing",
    author="Sadashiv",
    url="http://www.sadashivb.blogspot.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
    ],
    extras_require=dict(
        test=["pytest",
              "cov-core",
              "pytest-cov",
              ]),
    )
