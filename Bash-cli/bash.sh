#!/bin/bash
echo "This script is used for lookup service for pincode.
#Reading the pincode provided
read -p  "please enter the pincode: " pincode
echo The pin code passed : $pincode
cd /home/pin-code-CLI/
#copying the remote content to a file
curl -v -u username:password -O data.json "https://www.travel-advisory.info/api -k "
# processing and providing the details of the pincode using jq utility
echo "Details of the pincode `jq '.$pincode' data.json`"

