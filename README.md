Random PAC Name Generator
=========================

Random political action committee (PAC) name generator.

Dependencies
------------

This software must be installed to develop and build the code:
- [Python 2.7](http://www.python.org) for generating data.
- [fabric](http://docs.fabfile.org/en/1.4.3/index.html) for managing the execution and testing tasks.
- [nose](http://pypi.python.org/pypi/nose/) for running python tests.
- [NodeJS](http://nodejs) and [Mocha](http://visionmedia.github.com/mocha/) for executing javascript tests.

Tasks
-----

The following tasks are exposed through fabric:

- test
	Executes the python and javascript tests.
- test_python
	Executes the python tests.
- test_js
	Executes the javascript tests.
- gen_pac_trigrams
	Builds the PAC name trigrams JSON file.