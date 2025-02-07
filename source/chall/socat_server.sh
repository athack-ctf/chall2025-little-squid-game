#!/bin/bash

PORT=2025
SCRIPT_PATH="/home/chall/little-squid-game.py"

while true; do
    socat TCP-LISTEN:$PORT,reuseaddr EXEC:$SCRIPT_PATH,pty
    sleep $(shuf -i 1000-2000 -n 1 | awk '{print $1/1000}')
done