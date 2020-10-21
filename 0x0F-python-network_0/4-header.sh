#!/bin/bash
# Get the HTTP allowed methods by the server.
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id: 98"
