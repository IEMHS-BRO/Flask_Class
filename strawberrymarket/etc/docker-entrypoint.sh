#!/bin/bash

set -e

flask db upgrade
# gunicorn --bind :8080 --workers 2 --threads 8 --access-logfile - 'app:create_app()'
gunicorn --bind unix:/tmp/gunicorn.sock --workers 2 --threads 8 --reload --access-logfile - 'app:create_app()'