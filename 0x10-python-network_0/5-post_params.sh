#!/bin/bash
# Takes URL, sends POST request, display body
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"