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


@app.get ("/convert")
def convert ()
