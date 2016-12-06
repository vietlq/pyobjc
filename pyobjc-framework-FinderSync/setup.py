'''
Wrappers for the "FinderSync" framework on MacOS X.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

VERSION="3.2a1"

setup(
    name='pyobjc-framework-FinderSync',
    version="3.2",
    description = "Wrappers for the framework FinderSync on Mac OS X",
    long_description=__doc__,
    packages = [ "FinderSync" ],
    setup_requires = [
        'pyobjc-core>=3.2',
    ],
    install_requires = [
        'pyobjc-core>=3.2',
        'pyobjc-framework-Cocoa>=3.2',
    ],
    min_os_level="10.10",
)
