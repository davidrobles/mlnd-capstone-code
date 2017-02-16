shell:
	PYTHONPATH=. ipython

run:
	PYTHONPATH=. python ${file}

test:
	PYTHONPATH=. python -m unittest discover . -v

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-fig:
	rm figures/*
