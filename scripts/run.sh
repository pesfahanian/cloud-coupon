#!/bin/bash

gnome-terminal --title="AN-Couponing Django Server" -- /bin/sh -c \
    "python manage.py runserver 0.0.0.0:8800"
