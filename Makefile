.DEFAULT_GOAL := help
RED=\033[0;31m
GREEN=\033[0;32m
ORANGE=\033[0;33m
BLUE=\033[0;34m
NC=\033[0m # No Color

.PHONY: install
install: ## Install the dependencies
	@echo "${GREEN}🤖 Installing dependencies${NC}"
	python3 -m pip install --upgrade pip
	python3 -m pip install --editable .

.PHONY: dev
dev: install ## Install the development dependencies
	python3 -m pip install --editable ".[dev]"

.PHONY: lint
lint: ## Ensure code consistency
	@echo "${GREEN}🤖 Linting code${NC}"
	@ruff . --fix
	@black . --quiet
	@djlint templates --check --reformat --quiet --format-js --format-css

.PHONY: build
build: ## Generate the site
	@python3 generator.py build
	@python3 generator.py feed

.PHONY: serve
serve: ## Serve the website locally
	@echo "Ouvrir dans le navigateur : http://localhost:8000"
	@python3 -m http.server

.PHONY: help
help:
	@python3 -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

# See https://daniel.feldroy.com/posts/autodocumenting-makefiles
define PRINT_HELP_PYSCRIPT # start of Python section
import re, sys

output = []
# Loop through the lines in this file
for line in sys.stdin:
    # if the line has a command and a comment start with
    #   two pound signs, add it to the output
    match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        output.append("\033[36m%-10s\033[0m %s" % (target, help))
# Sort the output in alphanumeric order
output.sort()
# Print the help result
print('\n'.join(output))
endef
export PRINT_HELP_PYSCRIPT # End of python section
