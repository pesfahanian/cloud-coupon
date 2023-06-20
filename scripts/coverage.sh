#!/bin/bash

coverage run manage.py test \
    --verbosity=2

coverage html
