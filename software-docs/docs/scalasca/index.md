---
title: Information about scalasca
keywords:
  - Tools
---
# Scalasca

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | 2.6.1-cpeCray, 2.6.1-cpeGNU |

## General information

Scalasca is a tool for performance optimization of parallel programs by measuring and analyzing their runtime behavior.
https://www.scalasca.org/

## How to use

Scalasca makes use of the Cube performance report explorer and Score-P. You can check available modules of Scalasca using

```
ml PDC/<version>
ml spider Scalasca
ml avail Scalasca
```
For example, to load the module for Scalasca built with the cpeGnu 21.11 toolchain

```
ml PDC/<version>
ml Scalasca/2.6-cpeGNU-21.11
```
To display information on what dependency modules are loaded, and paths and environment variables are set, when loading a
Scalasca module

```
ml show Scalasca/2.6-cpeGNU-21.11
```
The Scalasca user guide
https://apps.fz-juelich.de/scalasca/releases/scalasca/2.6/docs/manual/
Getting started
https://apps.fz-juelich.de/scalasca/releases/scalasca/2.6/docs/manual/start.html
A full workflow example
https://apps.fz-juelich.de/scalasca/releases/scalasca/2.6/docs/manual/start_workflow.html

