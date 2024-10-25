from langflow.load import run_flow_from_json
from dotenv import load_dotenv
import requests
from typing import Optional
import json
import os

load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "e13455d5-ac2f-4bf8-8357-a0e750a46488"
APPLICATION_TOKEN = os.getenv("LANGFLOW_TOKEN")

def ask_ai(profile, question):
    TWEAKS = {
        "TextInput-twx0s": {
            "input_value": question
        },

        "TextInput-XwE87": {
            "input_value": profile
        },

    }

    result = run_flow_from_json(flow="Ask-AI.json",
                                input_value="message",
                                fallback_to_env_vars=True, # False by default
                                tweaks=TWEAKS)

    return result[0].outputs[0].results["text"].data["text"]



def get_macros(goals, profile):
    TWEAKS = {
    "TextInput-ecV6c": {
        "input_value": "goals"
    },
    "TextInput-tdvl6": {
        "input_value": "profile"
    },
    }
    return run_flow("", tweaks=TWEAKS, application_token=APPLICATION_TOKEN)

def run_flow(message: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/macros"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)

    return json.loads(response.json()["outputs"][0]["outputs"][0]["results"]["text"]["data"]["text"])