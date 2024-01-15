from fastapi import FastAPI
app= FastAPI()

@app.get("/health")
def health ():
kubectl get pods 

@app.get("/diag")  
def status()


@app.get ("/convert")
def convert ()
