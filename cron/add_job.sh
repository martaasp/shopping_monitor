#!/bin/bash

SCRIPT_FILE=$1
SCRIPT_ARG1=$2
SCRIPT_ARG2=$3
SCHEDULE=$4
CURRENT_FOLDER=$SCRIPT_ARG2

LOG_FOLDER="logs"
mkdir -p $CURRENT_FOLDER/$LOG_FOLDER/

COMMAND="/usr/bin/python3 $CURRENT_FOLDER/$SCRIPT_FILE $SCRIPT_ARG1 $SCRIPT_ARG2>> $CURRENT_FOLDER/$LOG_FOLDER/execution_log.log 2>&1"

# Comprueba si el trabajo ya está en crontab
crontab -l > mycron
if ! grep -qF -- "$COMMAND" mycron; then
    echo "Añadiendo tarea al crontab."
    echo "$SCHEDULE $COMMAND" >> mycron
    crontab mycron
else
    echo "La tarea ya está en crontab."
fi
rm mycron
