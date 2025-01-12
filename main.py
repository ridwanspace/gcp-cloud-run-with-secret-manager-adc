from fastapi import FastAPI
from google.cloud import secretmanager
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

def get_secret():
    project_id = os.getenv("PROJECT_ID")
    resource_name = os.getenv("RESOURCE_NAME")
    
    client = secretmanager.SecretManagerServiceClient()
    
    # Access the secret version
    response = client.access_secret_version(name=f"{resource_name}/versions/latest")
    
    # Return the decoded payload
    return response.payload.data.decode('UTF-8')

@app.get("/get-secret-value")
async def read_secret():
    try:
        secret_value = get_secret()
        return {"secret_value": secret_value}
    except Exception as e:
        return {"error": str(e)}
