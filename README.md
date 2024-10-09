# PDC-support-docs
Support documentation for  PDC Center for High Performance Computing.
These pages are written using Hugo, with the exception
of the support pages which are written in mkDocs.
Both tools however enable to publish material in MarkDown.

## Installation and using mkDocs

1. Find instructions at https://www.mkdocs.org/getting-started/
2. You need some extra extensions to render these documents
   1. In order to install attr_list, adminition and superfences
      `pip install mkdocs-material`

## Published material

The published webpages reside on different location depending if you are changing
the support documentation or that main website.

### Support documentation

The primary document is available in `mkdocs.yaml`
whereas all the markdown file are found in `mkdocs/docs`

## build site

To create material for both hugo and mkdocs just `make build` which will create a `site` folder with all html files
for mkdocs. This folder can the be moved to the actual site.

### Running site locally

In order to start mkdocs at the local computer use `make serve` from top level folder and navigate to https://127.0.0.1:8000

## publish site

In order to publish these documents to the official PDC webportal you need to have those specific access rights to KTH ITA.
Publishing is achieve by running command `make public` 
