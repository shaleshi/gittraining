from setuptools import setup, find_packages

setup(
    name="jiva",
    version="5.0",
    author="ZeOmega",
    author_email="info@zeomega.com",
    description="Jiva - Care Management Software",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools',
                     'Zope2',
                     'Chameleon'
		     'grok',
                     'megrok.jinja',		
     ],
 )
