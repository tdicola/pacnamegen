from fabric.api import *

# Test tasks
def test_python():
	print "Running python tests with nose."
	local("nosetests gen_pac_trigrams")

def test_js():
	print "Running javascript tests with mocha."
	local("mocha -u tdd ./web_tests/test_pacnamegen.js")

def test():
	test_python()
	test_js()

# Generate trigram task
def gen_pac_trigrams():
	with lcd("gen_pac_trigrams"):
		local("python parse_webk.py")
		local("python gen_pac_trigrams.py")