#!/usr/bin/env python
# pylint: disable=missing-docstring
from setuptools import setup


with open("README.rst") as readme:
    LONG_DESCRIPTION = readme.read()


setup(name='kiwitcms-tap-plugin',
      version='0.0',
      packages=['tap_plugin'],
      package_dir={'tap_plugin': '.'},
      description='Test Anything Protocol (TAP) plugin for Kiwi TCMS test case management system',
      long_description=LONG_DESCRIPTION,
      author='Kiwi TCMS',
      author_email='info@kiwitcms.org',
      license='GPLv3+',
      url='https://github.com/kiwitcms/tap-plugin',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.6',
          'Topic :: Software Development',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
      ])
