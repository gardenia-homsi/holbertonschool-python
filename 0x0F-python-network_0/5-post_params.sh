#!/bin/bash
# Get the HTTP allowed methods by the server.
curl "$1" -sX POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
