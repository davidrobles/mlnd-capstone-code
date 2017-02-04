shell:
	PYTHONPATH=. ~/anaconda2/bin/ipython

run:
	PYTHONPATH=. ~/anaconda2/bin/python ${ARGS}

test:
	PYTHONPATH=. python -m unittest discover . -v

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
