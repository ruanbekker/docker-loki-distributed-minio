#!/bin/sh
gunicorn app:app --bind 0.0.0.0:5000 --capture-output
#gunicorn app:app \
#	--workers 2 \
#	--threads 2 \
#	--bind 0.0.0.0:5000 \
#	--capture-output \
#	--access-logfile '-' \
#	--error-logfile '-'
