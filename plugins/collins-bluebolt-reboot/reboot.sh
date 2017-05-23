#!/usr/bin/env bash

telnet 192.168.0.23 <<EOF
#CYCLE 5:2
EOF
sleep 5
telnet 192.168.0.23 <<EOF
#CYCLE 4:2
EOF