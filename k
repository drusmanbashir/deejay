#!/bin/sh
# PYTHON SCRIPT PROCESS KILLER by GBO v0.1
# This script will look for all the lines containing $SOFTWARENAME in the process list, and close them
SOFTWARENAME='django.fcgi' # This is case insensitive
JOBPRESENT=$(ps -ef | grep -i $SOFTWARENAME | grep -v grep)
echo $JOBPRESENT
ps -ef | grep -i $SOFTWARENAME | grep -v grep | awk '{print $2}' | xargs kil
