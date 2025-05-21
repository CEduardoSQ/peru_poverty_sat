# Variables
PROJECT_NAME = peru_poverty_sat
ENV_FILE = environment.yml

# Commands
.PHONY: help set-env exp-env

## Help
help:
	@printf "Makefile commands:\n"
	@printf "  %-16s %s\n" "help" "Show this help message."
	@printf "  %-16s %s\n" "set-env" "Create or update the environment."
	@printf "  %-16s %s\n" "exp-env" "Export the active environment into a file."

## Set up the environment
set-env: $(ENV_FILE)
	@if conda env list | grep -q "* "; then \
		echo "Updating current environment..."; \
		conda env update --file=$(ENV_FILE) --prune; \
	else \
		echo "Creating $(PROJECT_NAME) environment..."; \
		conda env create --file=$(ENV_FILE); \
	fi

## Export the environment 
exp-env:
	@conda env export --from-history --name $(PROJECT_NAME) | sed '/^prefix:/d' > $(ENV_FILE); \
	echo "Environment file created: $(ENV_FILE)"; \
