#!/bin/bash
JOB_PATTERN=$1

# Comprueba si el trabajo ya está en crontab
crontab -l > mycron
grep -v "$JOB_PATTERN" mycron > modified_cron
crontab modified_cron

rm mycron modified_cron

echo "La tarea cron que contiene '$JOB_PATTERN' ha sido eliminada."
