# Makefile for building PDC website

# Default target
all: build

# Build PDC site
build:
	mkdocs build -f support-docs/mkdocs.yml 
	cp -r support-docs/site web/static/support-docs	
	mkdocs build -f software-docs/mkdocs.yml 
	cp -r software-docs/site web/static/software-docs	
	hugo --source "web"

# Runs a local server
serve:
	mkdocs build -f support-docs/mkdocs.yml 
	cp -r support-docs/site web/static/support-docs
	mkdocs build -f software-docs/mkdocs.yml 
	cp -r software-docs/site web/static/software-docs	
	hugo server --source "web"

serve_mkdocs:
	mkdocs serve -f support-docs/mkdocs.yml 

public:
	python3 update_docs.py

# Optional: Clean the site directory
clean:
	rm -rf support-docs/site
	rm -rf software-docs/site
	rm -rf web/public
	rm -rf web/static/support-docs
	rm -rf web/static/software-docs
