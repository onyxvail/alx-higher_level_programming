#!/bin/bash
# Get the URL request that is sent and
# displays the size of the body of the response.
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
