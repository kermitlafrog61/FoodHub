# FoodHub
[![Libraries Used](https://skillicons.dev/icons?i=py,nginx,django,docker,postgres)](https://skillicons.dev)

## Description

This is the backend for the FoodHub mobile app.

## Table of Contents

- [FoodHub](#foodhub)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Required prerequisites](#required-prerequisites)
    - [Installation process](#installation-process)
  - [Usage](#usage)
    - [Admin pannel](#admin-pannel)
  - [Acknowledgments](#acknowledgments)

## Installation

### Required prerequisites

- Docker Engine
- Docker Compose
- Make installed (optional)
- Python 3.11 (optional)

### Installation process
    
```bash
git clone https://github.com/kermitlafrog61/FoodHub.git
cd FoodHub
cp .env-example .env
```
Fill out all the necessary fields in .env

## Usage


```bash
make run
```
Wait untill all containers would start, then open localhost


### Admin pannel

Open /admin/ URL and fill out, what you wrote in .env


## Acknowledgments

This is a pet project for Vention Company in the lead of Toktosun.
