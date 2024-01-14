#!/bin/bash
echo "This script is used for lookup service for pincode.

read -p  "please enter the pincode: " pincode
echo The pin code passed : $pincode
cd /home/pin-code-CLI/
#copying the remote content to a file
curl -v -u username:password -O data.json "https://www.travel-advisory.info/api -k "
