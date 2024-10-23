---
title: Information about fleur
keywords:
  - Applications
  - Physics
---
# Fleur

## Installed versions

| Resource | Version |
|---|---|
| Dardel/cpe23.12 | MaX7.0 |
| Dardel/cpe23.03 | MaX7.0 |

## General information

FLEUR is a feature-full, freely available FLAPW (full-potential linearized augmented planewave) code, based on density-functional theory.
More information at https://www.flapw.de/

## How to use

Load the FLEUR module:

# 

```
$ module load fleur
```
Create an input file for testing fleur. The following link:

## 

```
https://www.flapw.de/MaX-4.0/CECAM-2019-tut/Day_1_first_steps/
```
contains intructions for a first calculation. In the first code block there is data for an Si crystal, copy that and place in a separate file you name si_data.txt for instance.
From the directory of that file you just created, type:

## 

```
$ inpgen < si_data.txt
```
Among several things, a file named inp.xml will be created. From the directory of the files run fleur by:

## 

```
$ fleur
```
An example shell script is:
:language: text

