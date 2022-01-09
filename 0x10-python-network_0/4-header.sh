#!/bin/bash
#takes URL, sends GET request display body
curl "$1" -sX GET -H "X-School-User-Id: 98"
