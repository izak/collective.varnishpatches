from setuptools import setup, find_packages

version = '0.1'

setup(
    name='collective.varnishpatches',
    version=version,
    description="Patches for Plone that makes life easier with varnish",
    long_description=open("README.txt").read(),
    # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        ],
    keywords='varnish languagetool caching cookie',
    author='Izak Burger',
    author_email='isburger@gmail.com',
    url='https://github.com/collective/collective.varnishpatches',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    package_data={'collective.varnishpatches': [
      '*.zcml'
    ]},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'collective.monkeypatcher',
    ],
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
    """,
    )
