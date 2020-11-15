import setuptools

with open("README.md", 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'First_python_package_Arpit', # this should be unique globally
	version = '0.0.1',
	author = 'Arpit Agarwal',
	author_email = 'arpitagarwal619@gamil.com',
	desciption = 'this is preprocessing package',
	long_description = = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_package(),
	classifiers = [
	'Programming Language:: Python :: 3',
	'License :: ODI Apporved :: MITI License',
	'Operating System :: OS Independent'],
	python_requires = '>=3.5'

	) 
