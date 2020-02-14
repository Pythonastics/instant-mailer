from setuptools import setup

with open("README.md") as f:
	rme = f.read()
	
setup(
	name="pymail",
	author="mischievousdev",
	author_email="miscdev.py@gmail.com",
	version="1.0.0",
	url="https://github.com/Pythonastics/pymail/tree/master"
	packages = ["pymail"],
	license="MIT",
	description="An API Wrapper of gmail to send instant mails using python",
	long_description=rme,
	keywords='gmail email wrapper',
	classifiers=[
		 'Development Status :: 5 - Production/Stable',
         'License :: OSI Approved :: MIT License',
         'Intended Audience :: Developers',
         'Natural Language :: English',
         'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.5',
         'Programming Language :: Python :: 3.6',
         'Programming Language :: Python :: 3.7',
         'Topic :: Internet',
         'Topic :: Software Development :: Libraries',
         'Topic :: Software Development :: Libraries :: Python Modules',
         'Topic :: Utilities',
	]
)