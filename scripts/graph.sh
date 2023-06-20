#!/bin/bash

exclude="-X AbstractUser,Permission,Group,UUIDModel,ToggleableModel,TemporalModel"

python manage.py graph_models --pydot couponing user wallet "$exclude" -g -o docs/schema.png
