#!/bin/bash

python manage.py migrate
python manage.py loaddata admin_user.json
