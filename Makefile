# Variables
PROJECT_NAME = peru_poverty_sat
ENV_FILE = environment.yml

# Commands
.PHONY: help env env-file 

## Make help
help:
	@printf "Makefile commands:\n"
	@printf "  %-16s %s\n" "env" "Create or update the virtual environment."
	@printf "  %-16s %s\n" "env-file" "Export the current environment to a file."
	@printf "  %-16s %s\n" "help" "Show this help message."

## Make the environment
env: $(ENV_FILE)
	@if conda env list | grep -q "* "; then \
		echo "Updating the current environment..."; \
		conda env update --file=$(ENV_FILE) --prune; \
	elif conda env list | grep -q "^$(PROJECT_NAME)"; then \
		echo "Updating the existing environment $(PROJECT_NAME)..."; \
		conda env update --name $(PROJECT_NAME) --file=$(ENV_FILE) --prune; \
		echo "Environment $(PROJECT_NAME) updated."; \
	else \
		echo "Creating the environment $(PROJECT_NAME)..."; \
		conda env create --file=$(ENV_FILE); \
	fi

## Make the environment file
env-file:
	@conda env export --from-history --name $(PROJECT_NAME) | sed '/^prefix:/d' > $(ENV_FILE); \
	echo "Environment file created: $(ENV_FILE)"; \
