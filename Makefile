install: 
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

package-uninstall:
	python3 -m pip uninstall --yes dist/*.whl

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 gendiff

tests:
	poetry run pytest