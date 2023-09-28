#!/bin/bash
# Get the URL request that is sent and
# displays the size of the body of the response.
curl -sI "$1" | awk -v FS=": " '/^Content-Length/{print $2}'
