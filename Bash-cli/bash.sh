#!/bin/bash
#copying the remote content to a file
curl -v -u username:password -O data.json "https://www.travel-advisory.info/api -k "
echo "This script is used for lookup service for pincode.
#Reading the pincode provided
read -p  "please enter the pincode separated by spaces: " pincode_names
cd /home/pin-code-CLI/
for pincode in $pincode_names
do 
# processing and providing the details of the pincode using jq utility
echo "Details for the pincode `jq '.$pincode' data.json`"
echo The pin code passed : $pincode_names
done






