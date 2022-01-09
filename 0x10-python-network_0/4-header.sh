#!/bin/bash
#takes URL, sends GET request display body
curl -sH "X-School-User-Id: 98" -X GET "$1"