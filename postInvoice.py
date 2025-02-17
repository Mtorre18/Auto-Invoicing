import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()


AUTH_HEADER = os.getenv("AUTH_HEADER")
API_SERVER =os.getenv("API_SERVER")
INV_ENDPOINT = os.getenv("INV_ENDPOINT")
BAQ_ENDPOINT = os.getenv("BAQ_ENDPOINT")

headers = {
    "Authorization": AUTH_HEADER,
    "Content-Type": "application/json"
    }

def post_invoice(payload):

    ds={
        "ds": {
            "APInvHed": [
            payload
            ]
        }
    }


    url = f"{API_SERVER}{INV_ENDPOINT}"

    try:
        response = requests.post(url, headers=headers, data=json.dumps(ds),verify=False)
        
        if response.status_code in [200, 201]:
            return {"success": True, "data": response.json()}
        else:
            return {"success": False, "status_code": response.status_code, "error": response.text}
    
    except Exception as e:
        return {"success": False, "error": str(e)}
    

def query_baq(baq_name, params=None):

    endpoint = f"{BAQ_ENDPOINT}{baq_name}"
    url = f"{API_SERVER}{endpoint}"
    

    try:
        response = requests.get(url, headers=headers, params=params, verify=False)
        

        if response.status_code == 200:
            data = response.json()
            return {"success": True, "data": data['value']}
        else:
            return {"success": False, "status_code": response.status_code, "error": response.text}
    
    except Exception as e:
        return {"success": False, "error": str(e)}


