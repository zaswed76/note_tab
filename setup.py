# -*- coding: utf-8 -*-

from os.path import join, dirname

from setuptools import setup, find_packages

import notetub

setup(
        name="note_tub",
        version=notetub.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=["PyQt5", "pyaml"],
        entry_points={
            'console_scripts':
                ['notetub = notetub.note_tub:main']
        }

)
