## Lint your code using pylint
.PHONY: lint
lint:
	python -m pylint .
## Create README.md from main.py
.PHONY: build
build:
	python main.py
## Format your code using black
.PHONY: black
black:
	python -m black .
## Run ci part
# .PHONY: ci
#         ci: precommit build black
