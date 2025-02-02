#!/bin/bash

PORT=2025
SCRIPT_PATH="/home/chall/little-squid-game.py"

while true; do
    socat TCP-LISTEN:$PORT,reuseaddr EXEC:$SCRIPT_PATH,pty
    sleep 1
done