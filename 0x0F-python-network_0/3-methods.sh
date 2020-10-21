#!/bin/bash
# Get the HTTP allowed methods by the server.
curl -sI "$1" | grep Allow | cut -f2- -d " "
