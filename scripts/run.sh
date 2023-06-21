#!/bin/bash

gnome-terminal --title="Cloud-Coupon Django Server" -- /bin/sh -c \
    "python manage.py runserver 0.0.0.0:8800"
