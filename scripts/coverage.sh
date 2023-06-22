#!/bin/bash

coverage run manage.py test \
    apps.coupon.tests \
    apps.user.tests \
    apps.wallet.tests \
    --verbosity=2 \

coverage html
