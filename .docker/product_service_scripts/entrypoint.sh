#!/bin/sh

set -e

. /venv/bin/activate

python ./product_service/app.py
