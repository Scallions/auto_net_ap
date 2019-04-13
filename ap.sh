#!/bin/bash

nohup /home/pi/whu-wlan.py > /dev/null 2>&1 &

nohup create_ap wlan0 eth0 SS 844120806 > /dev/null 2>&1 &