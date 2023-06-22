#!/bin/bash

coverage run manage.py test \
    apps.user.tests \
    --verbosity=2 \
    --parallel

coverage html
