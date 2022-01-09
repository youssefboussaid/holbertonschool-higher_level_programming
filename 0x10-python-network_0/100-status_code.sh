#!/bin/bash
# Displays the size of the status code of the response of a curl request
curl -s -o /dev/null -I -w "%{http_code}" "$1"
