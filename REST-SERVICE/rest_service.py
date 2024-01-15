from fastapi import FastAPI
app= FastAPI()

@app.get("/health")
def health ():
kubectl log pincode-service > healthcheck.log
kubetctl describe nodes >> healthcheck.log
grep "Not Ready" healthcheck.log
if [ $? -eq 0 ] ;
  then 
    print "NODES OR PODS ARE NOT RUNNING FINE. Please check"
else 
    print "NODES OR PODS ARE  RUNNING FINE"
fi;

@app.get("/diag")  
def status()
#import requests module
import requests 
# Making a get request
response = requests.get('https://www.travel-advisory.info/api') 
# print response 
print(response) 
# print request status_code 
print(response.status_code) 


@app.get ("/convert")
def get_key (val)
for key, value in $data.json
if val == value:
  return key
else
  return "key doesn't exist"
