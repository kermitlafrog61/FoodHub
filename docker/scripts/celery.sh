#!/bin/sh


celery -A core beat -l debug &
celery -A core worker -l info &

tail -f /dev/null