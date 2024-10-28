# Build file for paystation project

help:
	echo targets: tests clean_src clean_test clean zip

tests: 
	python -m unittest

clean_src:
	rm -rf paystation/__pycache__
	find paystation -name '*~' -delete

clean_test:
	rm -rf test/__pycache__
	find test -name '*~' -delete

clean: clean_src clean_test
	rm -rf __pycache__	
	find . -name '*~' -delete
	touch paystation.zip
	rm paystation.zip

zip: clean
	zip -r paystation.zip paystation test docs makefile
