#!/usr/bin/env bash
celery -A api beat -l info -S django