# Makefile for building PDC website

# Default target
all: build

# Build PDC site
build:
	mkdocs build

# Runs a local server
serve:
	mkdocs serve

public:
	python3 update_docs.py support

# Optional: Clean the site directory
clean:
	rm -rf site
